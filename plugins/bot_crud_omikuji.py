from slackbot.bot import respond_to
import random
import sys
from service.free_list import FreeList

@respond_to('酒みくじ|飲みたい|晩酌|三宅')
def omikuji_sake(message):
    sake_tag = random.choice(['ビール', 'ワイン', '日本酒', '焼酎', 'ウイスキー'])
    print(sake_tag)
    omikuji = FreeList.read_omikuji(sake_tag)
    message.reply(random.choice(omikuji))

@respond_to(r'^おみくじ\s+(\S+)')
def omikuji(message, list_name):
    omikuji = FreeList.read_omikuji(list_name)
    message.reply(random.choice(omikuji))

@respond_to(r'^om[ikuji]\s+(add)\s+(\S+)\s+(\S+)')
@respond_to(r'^om[ikuji]\s+(get)\s*(\S*)')
@respond_to(r'^om[ikuji]\s+(upd)\s+(\S+)\s+(\S+)')
@respond_to(r'^om[ikuji]\s+(del)\s+(\S+)\s+(\S+)')
def omikuji_facade(message, command_mode:str, list_name:str="", item_name:str=""):
    print("---------「omikuji_facade」がモード：" + command_mode + "でコールされました------------")
    COMMAND_MODE_CREATE = "add"
    COMMAND_MODE_READ   = "get"
    COMMAND_MODE_UPDATE = "upd"
    COMMAND_MODE_DELETE = "del"

    if (command_mode == COMMAND_MODE_CREATE):
        add_omikuji_list(message, list_name, item_name)
    elif (command_mode == COMMAND_MODE_READ):
        if (list_name is None or len(list_name) == 0):
            get_omikuji_list(message)
        else:
            get_omikuji_item(message, list_name)
    elif (command_mode == COMMAND_MODE_UPDATE):
        message.reply("更新機能は作成中")
        return
    elif (command_mode == COMMAND_MODE_DELETE):
        message.reply("削除機能は作成中")
        return
    else:
        message.reply("foobar")


def add_omikuji_list(message, list_name, item_name):
    print("---------「add_omikuji_list」がコールされました------------")
    # TODO 登録数チェック
    if (FreeList.create_omikuji(list_name, item_name)):
        msg_body = list_name + "を追加しました。"
    else:
        msg_body = list_name + "は既に登録済みです。"

    message.reply(msg_body)

def get_omikuji_list(message):
    print("---------「get_omikuji_list」がコールされました------------")
    omikuji_list = FreeList.read_omikuji_list()
    message.reply("```" + str(omikuji_list) + "```")

def get_omikuji_item(message, list_name):
    print("---------「get_omikuji_item」がコールされました------------")
    omikuji = FreeList.read_omikuji(list_name)
    message.reply("```" + str(omikuji) + "```")
