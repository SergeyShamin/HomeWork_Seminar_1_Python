'''Напишите программу, которая принимает на вход цифру, обозначающую день недели
 и проверяет, является ли этот день выходным'''

week_day = int(input('Введите число от 1 до 7: '))

if week_day <= 5:
    print('Будний день')
elif week_day == 6 or week_day == 7:
    print('Выходной день')
else:
    print('Введите другое число')