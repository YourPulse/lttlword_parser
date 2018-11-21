from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)
    main_div = soup.find('div', id = "main")
    elements = main_div.find_all('div', class_ = "col-sm-12 col-md-6 col-xs-120")
    for element in elements:
        print(element.prettify())

def main():
    parse(get_html("http://lttlword.ru/tag/rimworld-v1/"))

if __name__ == '__main__':
    main()