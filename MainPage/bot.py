import requests
import json
import datetime



#https://api.telegram.org/bot<token>/METHOD_NAME
token=
bot_url='https://api.telegram.org/bot'+token

def daytime_valid():
    now_for_valid=datetime.datetime.today()
    now_dayweek=int(now_for_valid.strftime('%w'))
    now_hour=int(now_for_valid.strftime('%H'))
    from_hour = 10 # менять и на фронте
    to_hour = 22
    valid_dayweek_mas = [0, 1, 2, 3, 4, 5, 6]
    print(now_dayweek, now_hour)
    if (from_hour<=now_hour and now_hour<to_hour and (now_dayweek in valid_dayweek_mas) ):
        return True
    else:
        return False

def to_bot_data_recall(dict):
    if (daytime_valid()==True):
        now = datetime.datetime.today()
        now = now.strftime('%d-%B %H:%M')
        text=str(now)+'\nЗАКАЗАН ОБРАТНЫЙ ЗВОНОК: \n\n'+dict['tel']
        params = {'chat_id': 572144380, 'text': text}
        bot_response = requests.post(bot_url + 'sendMessage', data=params)
        return None
    else:
        return None

def to_bot_data_massage(dict):
    now = datetime.datetime.today()
    now = now.strftime('%d-%B %H:%M')
    text=str(now)+'\nПРИШЛА ЗАЯВКА:\n\n'+'Ф.И.О: \n'+dict['name']+'\n\n'+'Телефон: \n' + dict['tel'] + '\n\n'+'Email: \n' + dict['Email'] + '\n\n' +'Сообщение: \n' + dict['mes']
    params = {'chat_id': 572144380, 'text': text}
    bot_response = requests.post(bot_url + 'sendMessage', data=params)
    return None





