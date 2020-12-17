import json
import time
import telebot
import requests
from bs4 import BeautifulSoup

with open("config.json") as file:
    config = json.load(file)

bot = telebot.TeleBot(config['API_TOKEN'])
page = 1




while True:
    domain = f"https://avatarko.ru/kartinki/kot/{page}"
    responce = requests.get(domain).text
    all_image = BeautifulSoup(responce, 'lxml').find_all('div', class_='position-relative')

    for image in all_image:
        storage_url = image.find('a').get('href')

        if storage_url != '':
            image = requests.get(storage_url).text
            result_link = BeautifulSoup(image, 'lxml').find('div', id='image_wrapper').find('img').get('src')
            image_bytes = requests.get(f"https://avatarko.ru{result_link}").content

            for channel in config['CHANNEL_LOGIN']:
                bot.send_message(channel, 'test')
                time.sleep(int(config['SLEEP']))

    page +=1



"""
config.json

{
  "API_TOKEN": "API_TOKEN",
  "CHANNEL_LOGIN": ["@first","@second"],
  "SLEEP": "3"

}
"""