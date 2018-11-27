from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv



class GetHtml:
    def __init__(self, url):
        self.url =  url

    def get_html(self):
        url =       self.url
        req =       Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response =  urlopen(req)
        html =      response.read()
        return html

    def parse(html):
        soup =      BeautifulSoup(html, features="html5lib")
        main_div =  soup.find('div', id = "main")
        return main_div



class GetInfo:
    def __init__(self, main_div):
        self.main_div = main_div


    def get_discription(self):
        section = self.main_div.find('section', class_='post_content')
        disc = section.find('p').text
        return disc

    def get_stats(self):
        li = self.main_div.find('ul', class_="meta text-muted list-inline meta_lttl").find('li', style="vertical-align: text-bottom;").find('em')
        if int(li.find('strong').text)==0:
            return 'Пока нет оценок'
        stats = li.find_all('strong')[1].text
        return stats

    def get_page(self):
        page_num = int(self.main_div.find_all('a', "page-numbers")[3].text)

        return page_num

GInf = GetInfo(GetHtml.parse(GetHtml('http://lttlword.ru/category/rimworld/mody').get_html()))
GDisc = GInf.get_discription()