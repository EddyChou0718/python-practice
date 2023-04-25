#coding=UTF-8

num = int(input('num: '))
revers = 0

while num > 0:
  revers = revers * 10 + num % 10
  num //= 10

print(revers)