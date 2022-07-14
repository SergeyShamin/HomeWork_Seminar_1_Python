'''Напишите программу, которая принимает на вход координаты
двух точек и находит расстояние между ними в 2D пространстве'''

import math

x1 = float(input('X1: '))
y1 = float(input('Y1: '))

x2 = float(input('X2: '))
y2 = float(input('Y2: '))


d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

print(d)