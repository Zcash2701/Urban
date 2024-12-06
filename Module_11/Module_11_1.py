"""
Кусочек из собственного маленького проекта, "Торговый телеграмм бот".
Данная функция отправляет запрос на биржу ByBit, и возвращает суточный объем торгов по монете.
Результат отправляется пользователю через телеграм бота.
"""

import telebot
import pandas as pd
from pybit.unified_trading import HTTP

myTelegaID = '11111'

teleBot = telebot.TeleBot('1111111111:TESTTOKEN')
session = HTTP(testnet=True)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def get_df_for_list_coins():
    final_data = pd.DataFrame()
    ticker = pd.DataFrame.from_records(session.get_tickers(category="linear",)["result"]["list"])
    final_data['symbol'] = ticker['symbol'].astype(str)
    final_data['volume'] = ticker['volume24h'].astype(str)

    return final_data


text = str(get_df_for_list_coins())
print(text)

#teleBot.send_message(myTelegaID, text, parse_mode="HTML", disable_web_page_preview=True)