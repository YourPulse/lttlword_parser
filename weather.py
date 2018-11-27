from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

def get_html(url):
    req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req)
    return resp.read()

def parse(html):
    soup = BeautifulSoup(html, features = "html5lib")
    main_div = soup.find('section', class_ = 'content').find('div', 'content_wrap').find('div', class_ = 'flexbox clearfix').find('div', class_ = 'main')
    temperatures = main_div.find('div', class_ = 'column-wrap').find('div', class_ = '__frame_sm').find('div', class_ = 'forecast_frame hw_wrap').find('div', class_ = 'tabs _center').find('a', class_ = 'tab tablink tooltip').find('div', class_ = 'tab_wrap').find('div', class_ = 'tab-content')
    t_temperatures = temperatures.find('div', class_ = 'tab-weather').find('div', class_ = 'js_meas_container temperature tab-weather__value').find('span', class_ = 'unit unit_temperature_c').find_all('span')
    t_temps = []
    for t_temp in t_temperatures: 
        t_temps.append(t_temp.text.strip())
    print('Temperature outside is: {}'.format(t_temps[0]))
def main():
    parse(get_html("https://www.gismeteo.com/weather-kirov-4292/"))

if __name__ == '__main__':
    main()
