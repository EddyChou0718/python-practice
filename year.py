#coding=UTF-8
year = int(input('年份: '))
ans = year % 4 == 0 and year % 100 != 0 or \
      year % 400 == 0

# (false_value, true_value)[boolean]
print(('否', '是')[ans])