import requests
from bs4 import BeautifulSoup

# 获取网易云音乐流行歌曲列表
url = 'https://music.163.com/discover/toplist?id=3779629'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
song_list = soup.find_all('a', {'class': 'msk'})

# 获取歌曲的名称和播放次数
songs = []
for song in song_list:
    song_name = song.get('title')
    song_url = 'https://music.163.com' + song.get('href')
    song_response = requests.get(song_url)
    song_soup = BeautifulSoup(song_response.text, 'html.parser')
    song_play_count = song_soup.find_all('strong', {'class': 's-fc6'})[0].text
    songs.append({'name': song_name, 'play_count': song_play_count})

# 按照播放次数排序，输出前10首歌曲
sorted_songs = sorted(songs, key=lambda x: int(x['play_count'].replace(',', '')), reverse=True)
for i in range(10):
    print(f"第{i+1}首歌曲: {sorted_songs[i]['name']}")
