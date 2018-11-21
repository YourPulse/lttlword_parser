from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.read()

def get_discription(html):
    soup = BeautifulSoup(html)
    main_div = soup.find('div', id = "main")
    section = main_div.find('section', class_='post_content')
    disc = section.find('p').text
    return disc

def get_stats(html):
    soup = BeautifulSoup(html)
    main_div = soup.find('div', id = "main")
    li = main_div.find('ul', class_="meta text-muted list-inline meta_lttl").find('li', style="vertical-align: text-bottom;").find('em')
    if int(li.find('strong').text)==0:
        return 'Пока нет оценок'
    stats = li.find_all('strong')[1].text
    return stats



def parse(html):
    soup = BeautifulSoup(html)
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
                'rating':       get_stats(get_html(article.header.div.h2.a['href'])) + ' из 5',
            }) 
    for mod in mods:
        print(mod)

def main():
    parse(get_html("http://lttlword.ru/category/rimworld/mody"))

if __name__ == '__main__':
    main()