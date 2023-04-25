# 最小公因數
def gcd(x, y):
  (x, y) = (y, x) if x > y else (x, y)

  for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
      return factor

# 最大公倍數
def lcm(x, y):
  return x * y // gcd(x, y)

x = int(input('X: '))
y = int(input('Y: '))

print(lcm(x,y))