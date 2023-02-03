# Программа для игры с конфетами человек против бота без интеллекта

from random import randint

"""
s = int(input("Enter the number of candies: "))
queue = randint(1, 3)
print(f'Now the turn is {"HUMAN" if queue==0 else "BOT"}')
while s > 0:
    if queue == 0:
        a = int(input("HUMAN, you can take no more than 28 candies, how math do you take?: "))
        print(f'HUMAN take {a} candies, balance is {s-a} candies')
        s = s-a
        queue = 1
    else:
        a = randint(1, 29)
        print(f'BOT take {a} candies, balance is {s-a} candies')
        s = s-a
        queue = 0
print(f'Winner is {"HUMAN" if queue==1 else "BOT"}')
"""

# Программа для игры с конфетами человек против бота c интеллектом ( порвет любого ) 

s = int(input("Enter the number of candies: "))
queue = randint(1, 3)
print(f'Now the turn is {"HUMAN" if queue==0 else "BOT"}')
while s > 0:
    if queue == 0:
        a = int(input("HUMAN, you can take no more than 28 candies, how math do you take ?: "))
        print(f'HUMAN take {a} candies, balance is {s-a} candies')
        s = s-a
        queue = 1
    else:
        if s <= 28:
            a = s
        elif ((s-2)//28) % 2 == 1:
            a = (s % 28-1) if s % 28 > 2 else 27+s % 28
        else:
            a = 1
        print(f'BOT take {a} candies, balance is {s-a} candies')
        s = s-a
        queue = 0
print(f'Winner is {"HUMAN" if queue==1 else "BOT"}')

