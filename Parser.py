from bs4 import BeautifulSoup
import requests

input_url = input('Введите ссылку на сайт в формате: (Пример: https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=): ')
# поиск в определённой зоне
url = str(input_url)
map = {}
id = 0

# максимальное количество страниц
max_pages = int(input('Количество страниц для парсинга: '))
print('Ожидайте результата.')
print('...')

for p in range(max_pages):
    cur_url = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=' + str(p+1)
    # делаем запрос и получаем html
    html_text = requests.get(cur_url).text
    # используем парсер lxml
    soup = BeautifulSoup(html_text, 'lxml')  # Переменная soup содержит полный HTML-код страницы с результатами поиска

    # получаем все элементы
    ad = soup.find_all('span',
                       class_='_93444fe79c--color_black_100--kPHhJ _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6')
    urls = soup.find_all('div', class_='_93444fe79c--container--kZeLu _93444fe79c--link--DqDOy')
    titles = soup.find_all('span', class_='_93444fe79c--color_primary_100--mNATk _93444fe79c--lineHeight_28px--whmWV _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_22px--viEqA _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6' )

    for i in range(len(ad)):
        adi = ad[i]
        ur = urls[i]
        nam = titles[i]
        id += 1
        map[id] = {}
        # находим название
        name = nam.find('span')
        # находим цену
        price = adi.find('span')
        # находим адрес
        address = str(ur.find('a'))[str(ur.find('a')).find('href') + 6:str(ur.find('a')).find('>')-1]
        if len(address) == 0:
            print("Максимальный номер страницы: %d" % (p))
            break
        map[id]["name"] = name
        map[id]["address"] = address
        map[id]["price"] = price

for i in map:
    print(i)
    print(*map[i]['name'])
    print(*map[i]['address'])
    print(*map[i]['price'], sep='\n')