import random
import math

def play():
    user = input("what is your choice ? ('r' for rock, 'p' for paper, 's' for scissor) : ")
    user = user.lower()
    computer = random.choice(['p','s','r'])

    if user == computer:
        return (0, user, computer)
    
    # r>s,s>p,p>r
    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the computer
    # winning condition: r>s,s>p,p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone win best of n games
    # to win, you must win (n/2) games {i.e. 2/3,3/5,4/7}
    player_win = 0
    computer_win = 0
    win_necessary = math.ceil(n/2)
    while player_win < win_necessary and computer_win < win_necessary:
        result, user, computer = play()
        # for tie
        if result == 0:
            print("it is a tie. you and computer both chosenn {}.".format(user))
        # for win 
        elif result ==1:
            player_win += 1
            print('you chose {} and computer chose {} you win.'.format(user, computer))
        else:
            computer_win +=1
            print('you chose {} and computer chose {} you loss *SORRY* .'.format(user, computer))
        print('\n')
    if player_win > computer_win:
        print('you have won the best of games. *CONGRATES* .'.format(n))
    else:
        print('Unfortunatly, computer has won the best of {} games. Better luck Next Time .'.format(n))


if __name__=='__main__':
    play_best_of(3)