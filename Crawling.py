import requests
from bs4 import BeautifulSoup

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg='
for i in range(1, 5):
    site = '{}{}'.format(url, i)
    print(site)

genie = []

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg='

for i in range(1, 5):
    site = '{}{}'.format(url, i)
    request = requests.get(site, headers=header)
    soup= BeautifulSoup(request.text, 'html.parser')
    tbody = soup.find('tbody')
    titles = tbody.findAll('a', {'class':'title'})
    artists = tbody.findAll('a', {'class': 'artist'})

    for i in range(50):
        title = titles[i].text.strip()
        artist = artists[i].text.strip()
        genie.append((title, artist))

# 결과 출력
print("지니뮤직 TOP 200:")
for i, song in enumerate(genie, start=1):
    print(f"{i}위. {song[0]} - {song[1]}")