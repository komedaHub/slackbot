from slackbot.bot import respond_to
import random
import json
import sys
import urllib

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
