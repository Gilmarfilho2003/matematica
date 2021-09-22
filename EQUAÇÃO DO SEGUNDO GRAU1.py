from time import sleep
print('\033[1;36m-=-\033[m' * 8)
print('\033[1;4;32mEQUAÇÃO DO SEGUNDO GRAU\033[m')
print('\033[1;36m-=-\033[m' * 8)
a = 0
while a == 0:
    a = int(input('DIGITE O COEFICIENTE DE A: '))
    if a == 0:
        print('\033[31mO VALOR DE "A" NÃO PODE SER ZERO.\033[m')
b = int(input('DIGITE O COEFICIENTE DE B: '))
c = int(input('DIGITE O COEFICIENTE DE C: '))
if a == 1:
    print(f'x² + {b}x + {c} = 0')
elif a == -1:
    print(f'-x² + {b}x + {c} = 0')
else:
    print(f'{a}x² + {b}x + {c} = 0')
print('\033[36mCALCULANDO...\033[m')
sleep(2)
delta = b ** 2 - 4 * a * c
print(f'\033[1;4mO RESULTADO DE DELTA É {delta}\033[m')
if delta < 0:
    print('\033[31mX¹ e X² NÃO EXISTE NO CONJUNTO DOS NÚMEROS REAIS\033[m')
else:
    x1 = (- b + delta ** 0.5) / (2 * a)
    print(f'O VALOR DE X¹ É {x1:.2f}')
    x2 = (- b - delta ** 0.5) / (2 * a)
    print(f'O VALOR DE X² É {x2:.2f}')
    
    print(f'\033[1;33mS = ({x1:.2f}, {x2:.2f})\033[m')
