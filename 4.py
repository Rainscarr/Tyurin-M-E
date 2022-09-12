seconds = int(input('Введите кол-во секунд: '))

day = 86400
hour = 3600
minute = 60

days = seconds / day
seconds = seconds % day
hours = seconds / hour
seconds = seconds % hour
minutes = seconds / minute
seconds = seconds % minute

print(days,hours,minutes, seconds)
