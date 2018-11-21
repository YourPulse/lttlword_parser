from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.read()

def get_discription(html):
    soup = BeautifulSoup(html, features="html5lib")
    main_div = soup.find('div', id = "main")
    section = main_div.find('section', class_='post_content')
    disc = section.find('p').text
    return disc

def get_stats(html):
    soup = BeautifulSoup(html, features="html5lib")
    main_div = soup.find('div', id = "main")
    li = main_div.find('ul', class_="meta text-muted list-inline meta_lttl").find('li', style="vertical-align: text-bottom;").find('em')
    if int(li.find('strong').text)==0:
        return 'Пока нет оценок'
    stats = li.find_all('strong')[1].text
    return stats

def get_page(html):
    soup = BeautifulSoup(html, features="html5lib")
    main_div = soup.find('div', id = "main")
    page_num = int(main_div.find_all('a', "page-numbers")[3].text)

    return page_num

def parse(html):
    soup = BeautifulSoup(html, features="html5lib")
    main_div = soup.find('div', id = "main")
    rows = main_div.find_all('div', class_ = "row row-lttl")

    mods = []

    for row in rows:
        articles = row.find_all('article')
        for article in articles:
            mods.append({
                'mod_name':     article.header.div.h2.a.text, 
                'tags':         [tag.text for tag in article.header.find('div', class_ = 'meta_tags').p.find_all('a')],
                'discription':  get_discription(get_html(article.header.div.h2.a['href'])),
                'date':         article.header.li.time.text,
                'rating':       get_stats(get_html(article.header.div.h2.a['href'])),
            }) 
    
    return mods

def save(mods, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Mod Name', 'Tags', 'Discription', 'Date', 'Rating'))

        for mod in mods:
            writer.writerow((mod["mod_name"], ','.join(mod["tags"]), mod["discription"], mod["date"], mod["rating"]))

def main():
    max_page = get_page(get_html("http://lttlword.ru/category/rimworld/mody"))
    mods = []
    print('Всего страниц найдено: {}'.format(max_page))
    for page in range(1, max_page):
        print("Парсинг {}%".format(page  / max_page * 100))
        mods.extend(parse(get_html("http://lttlword.ru/category/rimworld/mody/page/" + str(page))))
    
    print("Парсинг завершен!")

    save(mods, 'mods.csv')

    print('Готово!')

if __name__ == '__main__':
    main()