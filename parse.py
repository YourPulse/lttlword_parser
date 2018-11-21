from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)
    main_div = soup.find('div', id = "main")
    rows = main_div.find_all('div', class_ = "row row-lttl")

    mods = []

    for row in rows:
        articles = row.find_all('article')
        for article in articles:
            mods.append({
                'mod_name': article.header.div.h2.a.text 

            })
    print(mods)

def main():
    parse(get_html("http://lttlword.ru/tag/rimworld-v1/"))

if __name__ == '__main__':
    main()