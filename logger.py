from datetime import datetime as dt
from time import time

def record (data):
    time = dt.now().strftime('%H: %M')              #часы минуты 
    with open('log.csv', 'a') as file:              #запись в файл, даже если его нет.
        file.write('{}; time of action; {}\n'              # слева время, time of action справа ответ от действия и переход на новую строку
                    .format(time, data))

