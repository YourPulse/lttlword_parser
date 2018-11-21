from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_html(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html)

def main():
    print(get_html("http://lttlword.ru/tag/rimworld-v1/"))

if __name__ == '__main__':
    main()