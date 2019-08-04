from slackbot.bot import respond_to
import random
import math
import json

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))

@respond_to('酒')
def alcohol_roulette(message):
    message.reply(random.choice(['ビール', 'ワイン', '日本酒', '焼酎', 'ウイスキー']))

@respond_to(r'^calcprice|cip (\d+) (\d+)')
def calc_include_tax_price(message, arg1, arg2):
    text = message.body['text'].split(" ")
    base_price = int(arg1)
    tax_rate = int(arg2)
    include_tax_price = math.floor(base_price + (base_price * (tax_rate / 100)))
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
    # msg = 'あなたの送ったメッセージは\n```' + text + '```'
    # message.reply(msg)
    message.reply(str(include_tax_price))

@respond_to('help')
def reply_help(message):
    attachments = [
        {
            'color': "#FF8000",
            'fields': [
                {'title': "コマンド", 'value': "help", 'short': True},
                {'title': "説明", 'value': "ヘルプを表示します", 'short': True},
            ]
        }
    ]
    message.send_webapi('コマンド一覧', json.dumps(attachments))
