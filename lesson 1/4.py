# -*- coding: utf-8 -*-
seconds = int(input('Введите кол-во секунд: '))

day = 86400
hour = 3600
minute = 60

days = int(seconds / day)
seconds = seconds % day
hours = int(seconds / hour)
seconds = seconds % hour
minutes = int(seconds / minute)
seconds = seconds % minute

print(f'{days}:{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
