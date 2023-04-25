from random import randrange, randint, sample

def display(balls):
  # enumerate => [(index1, value1), (index2, value2)......]
  for index, ball in enumerate(balls):
    if index == len(balls) - 1:
      print('|', end = ' ')
    print('%02d' % ball, end = ' ')
  print()

def random_select():
  # 產生所有彩球
  red_balls = [x for x in range(1, 42)]
  selected_balls = []

  # 隨機選6顆
  selected_balls = sample(red_balls, 6)
  # 排序
  selected_balls.sort()
  # 加入特別號
  selected_balls.append(randint(1, 6))

  return selected_balls

def main():
  n = int(input('注數: '))

  for _ in range(n):
    display(random_select())


if __name__ == '__main__':
  main()