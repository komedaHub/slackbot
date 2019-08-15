from slackbot.bot import respond_to
import random
import math
import json
import sys
import urllib
from service.calc_price import CalcPrice
from service.free_list import FreeList
# from service import free_list.FreeList

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))

@respond_to('酒')
def roulette_alcohol(message):
    message.reply(random.choice(['ビール', 'ワイン', '日本酒', '焼酎', 'ウイスキー']))

# @respond_to(r'^omikuji|omi|okj|list add (\S*) (\S*)')
def add_omikuji_list(message, list_name, item_name):
    FreeList.add(list_name, item_name)
    message.reply(list_name + "に" + item_name + "を追加しました。")

# @respond_to(r'^omikuji|omi|okj|list showall')
def show_omikuji_list(message):
    omikuji_list = FreeList.read_header()
    message.reply("```" + str(omikuji_list) + "```")

@respond_to(r'^omikuji|omi|okj|list show (\S*)')
def show_omikuji(message, list_name):
    omikuji = FreeList.read_article(list_name)
    message.reply("```" + str(omikuji) + "```")

@respond_to('電車遅れてる？')
def train(message):
    url = 'https://tetsudo.rti-giken.jp/free/delay.json'
    html = urllib.request.urlopen(url)
    jsonfile = json.loads(html.read().decode('utf-8'))

    for json in jsonfile:
        name = json['name']
        company = json['company']
        text = company + name + 'が遅延してるぴょん♪'
        message.send(text)

@respond_to('usagi')
def reply_hello(message):
    attachments = [
        {
            "color": "#3104B4",
            "fields": [
                {
                    "title": "場所",
                    "value": "東京駅"
                },
                {
                    "title": "時間",
                    "value": "19:00"
                }
            ],
            "footer": "usagi-san",
            "footer_icon": "https://pics.prcm.jp/db36726f85742/67433428/jpeg/67433428.jpeg"
        }
    ]
    message.send_webapi('集合場所', json.dumps(attachments))
