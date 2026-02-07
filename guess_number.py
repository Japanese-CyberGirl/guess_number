from random import randint

x = randint(0,100)

answer = int(input())

while (answer != x):
    if answer < x:
        print('Ваше число меньше того, что загадано')
        answer = int(input())
        continue
    if answer > x:
        print('Ваше число больше того, что загадано')
        answer = int(input())
        continue
print('Отличная интуиция! Вы угадали число :)')
