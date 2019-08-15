from slackbot.bot import respond_to
from service.calc_price import CalcPrice

@respond_to(r'^calincprice|cip (\d+) (\d+)')
def calc_include_tax_price(message, base_price:int, tax_rate:int):
    calc_price = CalcPrice()
    include_tax_price = calc_price.include_tax_price(int(base_price), int(tax_rate))
    # 送信メッセージを作る。
    msg = str(base_price) + "円の税込価格は\n"
    msg += "```" + str(include_tax_price) + "円```\nです。"
    message.reply(msg)

@respond_to(r'^calexcprice|cep (\d+) (\d+)')
def calc_exclude_tax_price(message, sales_price:int, tax_rate:int):
    calc_price = CalcPrice()
    exclude_tax_price = calc_price.exclude_tax_price(int(sales_price), int(tax_rate))
    # 送信メッセージを作る。
    msg = str(sales_price) + "円の税抜価格は\n"
    msg += "```" + str(exclude_tax_price) + "円```\nです。※端数分、誤差が生じます。"
    message.reply(msg)
