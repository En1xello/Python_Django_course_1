import requests
import time
from datetime import datetime


from Notebooks.enums import ServerCodes


while True:
    try:
        a = requests.get('https://yandex.ru')
        print(a)
        time.sleep(60)
        if a == ServerCodes.CODE200.value:
            pass
        elif a == ServerCodes.CODE503.value:
            print('ошибка сайта')
        else:
            print('иная ошибка')
    except requests.exceptions.ConnectionError:
        error_time = datetime.now()
        print('Сервер упал!\n' + str(error_time))
