from slackbot.bot import respond_to
import random
import math
import json
import sys
from service.free_list import FreeList
# from service import free_list.FreeList

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))

@respond_to('酒')
def roulette_alcohol(message):
    message.reply(random.choice(['ビール', 'ワイン', '日本酒', '焼酎', 'ウイスキー']))

@respond_to(r'^foo (\S*)')
def roulette_free_collection(message, arg1):
    # aaa = free_list()
    # free_list.FreeList.add(arg1)
    FreeList.add(arg1)
    message.reply(random.choice(['ビール', 'ワイン', '日本酒', '焼酎', 'ウイスキー']))

@respond_to(r'^calcprice|cip (\d+) (\d+)')
def calc_include_tax_price(message, arg1, arg2):
    base_price = int(arg1)
    tax_rate = int(arg2)
    include_tax_price = math.floor(base_price + (base_price * (tax_rate / 100)))
    # 送信メッセージを作る。
    msg = str(base_price) + "の税込価格は\n"
    msg += "```" + str(include_tax_price) + "円```\nです。"
    message.reply(msg)

@respond_to('help')
def reply_help(message):
    attachments = [
        {
            'color': "#FF8000",
            'fields': [
                {'title': "コマンド", 'value': "help", 'short': True},
                {'title': "説明", 'value': "ヘルプを表示します", 'short': True},
            ]
        },
        {
            'color': "#FF8000",
            'fields': [
                {'title': "コマンド", 'value': "calcprice|cip 本体価格 消費税率(%)", 'short': True},
                {'title': "説明", 'value': "税込価格を表示します。", 'short': True},
            ]
        }
    ]
    message.send_webapi('コマンド一覧', json.dumps(attachments))
