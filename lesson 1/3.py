# -*- coding: utf-8 -*-
age = int(input('Введите ваш возраст: '))
name = input('Введите ваше имя: ')
if (age > 0) and (age < 75) and (name != 'Иван'):
    if age >= 16:
        print('Поздравляем вы поступили в ВГУИТ')
    else:
        print('Сначала нужно окончить школу! Осталось лет: ', 16 - age)

    





