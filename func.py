import requests
from bs4 import BeautifulSoup
import random
import time
import csv  # CSV 파일 처리를 위해 import

def m000(a, c):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= c:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m100(a):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 100:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m50(a):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 50:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m10(a):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 10:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')


def m000(a, c):
    print(a)
    time.sleep(1)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= c:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 아티스트: {artist}')

def m_random(d):
    print(d)
    time.sleep(1)
    print("[좋아요! 제가 열심히 찾아서 사용자님께 노래를 한 곡 추천할게요.]")
    time.sleep(1)
    print(f"[두구두구둥...]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.select('tr[data-song-no]')
        song_list = []

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            song_list.append((rank, title, artist))

        random_song = random.choice(song_list)
        time.sleep(1)
        print(f"[이 노래가 좋을 거 같아요!]")
        time.sleep(1)
        print(f'\n[추천 곡: {random_song[1]} | 아티스트: {random_song[2]}]')
    else:
        print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')


def m_save_csv(d):
    filename="melon_top100.csv"
    song_list = []
    print(d)
    time.sleep(1)
    print(f"[멜론 Top 100 차트 데이터를 '{filename}' 파일로 저장합니다.]")
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            # Store as tuple (rank, title, artist)
            song_list.append((rank, title, artist))
    else:
         print(f'[웹 페이지를 가져오는 데 실패했어요. T.T | 상태 코드: {response.status_code}]')
         print("===================") # Add separator
         return # Exit the function if scraping failed


    if not song_list:
        print("[저장할 차트 데이터가 없습니다.]")
        print("===================") # Add separator
        return

    # 2. CSV 파일 쓰기
    try:
        # newline='' : CSV 파일에 빈 줄이 추가되는 것을 방지 (특히 Windows)
        # encoding='utf-8-sig' : Excel에서 한글이 깨지지 않도록 함 (BOM 포함 UTF-8)
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            # Use csv.writer for lists of tuples/lists
            writer = csv.writer(csvfile)

            # Write header row manually
            writer.writerow(['순위', '제목', '아티스트'])

            # Write data rows
            writer.writerows(song_list)

        print(f"[성공: '{filename}' 파일에 Top {len(song_list)} 차트를 저장했습니다.]")
    except IOError as e:
        print(f"[오류: 파일 쓰기 중 문제가 발생했습니다 - {e}]")
    except Exception as e:
        print(f"[오류: CSV 저장 중 예상치 못한 오류 발생 - {e}]")

    print("===================") # Add separator