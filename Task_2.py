'''Напишите программу для. проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат'''

bool_vals = [ False, True ]

is_correct = True

for x in bool_vals:
    for y in bool_vals:
        for z in bool_vals:
            left = not (x or y or z)
            right = (not x) or (not y) or (not z)
            
            if left != right:
                is_correct = False
            
            print(str(left) + ' = ' + str(right), x, y, z)
            
if is_correct:
    print('Утверждение истинно')
else:
    print('Утверждениие не истинно')