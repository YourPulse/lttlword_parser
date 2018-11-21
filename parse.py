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

def parse(html):
    soup = BeautifulSoup(html)
    main_div = soup.find('div', id = "main")
    rows = main_div.find_all('div', class_ = "row row-lttl")

    mods = []

    for row in rows:
        articles = row.find_all('article')
        for article in articles:
            mods.append({
                'mod_name': article.header.div.h2.a.text, 
                'discription': get_discription(get_html(article.header.div.h2.a['href']))
            }) 
    for mod in mods:
        print(mod)

def main():
    parse(get_html("http://lttlword.ru/tag/rimworld-v1/"))

if __name__ == '__main__':
    main()