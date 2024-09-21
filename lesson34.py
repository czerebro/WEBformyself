# Парсинг

# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html

# https://pypi.org/project/beautifulsoup4/

# https://python-scripts.com/beautifulsoup-parsing?ysclid=m1cor2c388656093031
# https://habr.com/ru/companies/ruvds/articles/796885/

# В терминале: pip -V чтобы узнать версию pip
# pip freeze Чтобы узнать список установленных пакетов

from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', 'liga-news-item')

results = []
for item in news:
    title = item.find('span', 'd-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

# режим w - Если файла нет он создаётся
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
    i += 1
f.close()