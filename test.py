import requests
from bs4 import BeautifulSoup

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'  # 멜론의 최신 차트 URL로 확인 필요

# 헤더 설정 (멜론은 User-Agent 확인을 통해 봇 접근을 차단할 수 있으므로 설정이 필요할 수 있음)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)
# response = requests.get(url)
print(response) # 응답값 출력
# print(response.text) # 요청한 데이터 문서 보기
# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a

title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').get_text()
print(title)

title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').get_text()
print(title)

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

for i in range(1, 11):
    print(i)