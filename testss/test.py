number_of_sticks = int(input('Enter number sticks:  '))
player1 = str(input('Player 1 enter you name: '))
player2 = str(input('Player 2 enter you name: '))
player_turn = 1


def can_taken(sticks_taken,remaining_sticks):
    return sticks_taken >= 1 and sticks_taken <= 3 and sticks_taken <= remaining_sticks


def switch_player_turn(turn):
    return player1 if player_turn == player2 else player2


def this_end_games(sticks):
    return number_of_sticks <= 0


while not this_end_games(number_of_sticks):
    print(f'How many sticks you take? \tRemained {number_of_sticks}')
    taken = int(input())

    if not can_taken(taken, number_of_sticks):
        if taken > number_of_sticks:
            print("You tried to take more than on the table")
        else:
            print(f'You tried to take {taken}. Allowed to take 1,2,3 sticks')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if this_end_games(number_of_sticks):
        print(f'No more stikcs in game. \nPlayer {player_turn} has lost!')
        break

    player_turn = switch_player_turn(player_turn)