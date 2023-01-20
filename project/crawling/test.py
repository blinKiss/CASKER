# 라이브러리 설치
# 터미널 >
# pip install requests
# pip install bs4
# pip install lxml


import requests
from bs4 import BeautifulSoup

# 특정 사이트의 html 가져오기
url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=74977"
html = requests.get(url)

print(html)


# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# 영화 제목
h3 = soup.find('h3', class_='h_movie')
a = h3.find('a')
text = a.get_text()

print(text)


# 특정 사이트의 html 가져오기
url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=74978"
html = requests.get(url)

print(html)


# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# 영화 제목
h3 = soup.find('h3', class_='h_movie')
s = h3.find('strong', class_='h_movie2')
t = s['title']
a = h3.find('a')
text = a.get_text()

print(t)
