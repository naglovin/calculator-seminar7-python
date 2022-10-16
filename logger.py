from datetime import datetime as dt
from time import time

def record (data):
    time = dt.now().strftime('%H: %M')
    with open('log.csv', 'a') as file:
        file.write('{}; действие; {}'
                    .format(time))
                    
