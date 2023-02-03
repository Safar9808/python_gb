# Создайте программу для игры с конфетами человек против человека

from random import randint
s = int(input("Enter the number of candies: "))
queue= randint(1,3)
print(f'Now the turn is {"HUMAN" if queue==0 else "BOT"}')

# только начал писать, время от времени буду пушить в гитхаб