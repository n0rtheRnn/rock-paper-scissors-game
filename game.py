human_turn = 'Paper'
computer_turn = 'Rock'

if human_turn == computer_turn:
    print('Draw!')
elif human_turn == 'Rock' and computer_turn == 'Scissors':
    print('Human wins!')
elif human_turn == 'Paper' and computer_turn == 'Rock':
    print('Human wins!')
elif human_turn == 'Scissors' and computer_turn == 'Paper':
    print('Human wins!')
else:
    print('Computer wins!')
