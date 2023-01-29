from bs4 import BeautifulSoup
import requests
import fake_useragent
import os

'''
directory = "music_pictures"
parent_dir = "C:/Users/user/Desktop/wallpaperscraft"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
'''

storage_number = "catalog/music/page1"
#link = "https://wallpaperscraft.ru/catalog/music/"
link = "https://wallpaperscraft.ru"

# response = requests.get(link).text
response = requests.get(f'{link}/{storage_number}').text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', class_ = 'wallpapers wallpapers_zoom wallpapers_main')
all_images = block.find_all('li', class_ = 'wallpapers__item')

for image in all_images:
    '''
    print(image)
    break
    '''
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'{link}{image_link}').text
    print(download_storage)
