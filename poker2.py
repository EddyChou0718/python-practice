from poker import Card, Poker, Player, Board

def get_key(card):
  return (card.suite, card.face)

def main():
  p = Poker()
  p.shuffle()
  players = [Player('test1'), Player('test2'), Player('test3'), Player('test4'), Player('test5')]
  board = Board()
  burned = []

  def deal(target, num):
    if target == 'players':
      for _ in range(num):
        for player in players:
          player.get(p.next)

    elif target == 'board':
      board.burn(p.next)
      for _ in range(num):
        board.get(p.next)

  deal('players', 2)
  deal('board', 3)
  deal('board', 1)
  deal('board', 1)

  for player in players:
    print(player.name + ':', end=' ')
    player.arrange(get_key)
    print(player.cards_on_hand)

  print('Board:', end=' ')
  print(board.cards_on_board)
  print('Burned:', end=' ')
  print(board.burned)

if __name__ == '__main__':
  main()