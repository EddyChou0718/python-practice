from numpy import random

x = random.randint(1, 10)

ans = int(input('Please enter a number: '))

while ans != x:
  if ans < x:
    print('bigger')

  if ans > x:
    print('smaller')

  ans = int(input('Please enter a number: '))

print('bingo! The ans is ' + str(x))
