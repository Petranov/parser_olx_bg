import requests
from bs4 import BeautifulSoup
import fake_useragent

link = 'https://www.olx.bg/'
user_agent = fake_useragent.UserAgent().random
headers = {
    'User-agent' : user_agent
}
def pars(link):
    response = requests.get(link, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_='css-127xiqh')
    obyavi = block.find_all('div', class_= 'css-2v45ok')

    number = 1
    with open('pars.txt', 'a') as file:
        for finall in obyavi:
            name = finall.find('p', class_='css-ki4ei7 er34gjf0')
            price = finall.find('p', class_='css-15fj1il er34gjf0')
            city = finall.find('p', class_='css-1pzx3wn er34gjf0')
            result = {
                'Номер объявления': number,
                'Имя:' : name.text,
                'Прайс:' : price.text,
                'Город:' : city.text
            }
            file.write(f"Номер объявления: {result['Номер объявления']}, Имя: {result['Имя:']}, Прайс: {result['Прайс:']}, Город: {result['Город:']}\n")
            number += 1


pars(link)
