from slackbot.bot import respond_to
import json

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
                {'title': "コマンド", 'value': "calincprice|cip 本体価格 消費税率(%)", 'short': True},
                {'title': "説明", 'value': "税込価格を表示します。", 'short': True},
            ]
        },
        {
            'color': "#FF8000",
            'fields': [
                {'title': "コマンド", 'value': "calexcprice|cep 税込価格 消費税率(%)", 'short': True},
                {'title': "説明", 'value': "税抜価格を表示します。", 'short': True},
            ]
        },
        {
            'color': "#FF8000",
            'fields': [
                {'title': "コマンド", 'value': "omikuji|omi|okj|list add key_name value_name", 'short': True},
                {'title': "説明", 'value': "key名のおみくじに追加する。", 'short': True},
            ]
        }
    ]
    message.send_webapi('コマンド一覧', json.dumps(attachments))
