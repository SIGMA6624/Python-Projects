# if it doesn't work here, open a new notebook and paste this code in a new cell
from IPython.display import clear_output
import random
import time

def display_board(board):
    # a "clear screen" command; this only works in Jupyter Notebook
    clear_output()
    
    for line in range(12):
        if line < 4:
            if line == 2:
                print(f' {board[1]} | {board[2]} | {board[3]} ')
            else:
                print('   |   |   ')
        elif line == 4 or line == 8:
            print('-----------')
        elif line > 4 and line < 8:
            if line == 6:
                print(f' {board[4]} | {board[5]} | {board[6]} ')
            else:
                print('   |   |   ')
        elif line > 8:
            if line == 10:
                print(f' {board[7]} | {board[8]} | {board[9]} ')
            else:
                print('   |   |   ')
                
def choose_first():
    firstplayer = random.randint(0,1)
    print(f'We will start with player {firstplayer+1}!')
    return firstplayer

def set_marker(playerturn):
    playermarkerlist = ['', '']
    while True:
        mark = input(f"Ok, player {playerturn + 1}, will you play with 'X' or 'O'? Choose here: ").upper()
        if mark == 'X':
            playermarkerlist[playerturn] = mark
            if playerturn == 0:
                playermarkerlist[1] = 'O'
            elif playerturn == 1:
                playermarkerelist[0] = 'O'
            break

        elif mark == 'O':
            playermarkerlist[playerturn] = mark
            if playerturn == 0:
                playermarkerlist[1] = 'X'
            elif playerturn == 1:
                playermarkerlist[0] = 'X'
            break
        else:
            print("Not 'X' or 'O'. Try again.")

    print(f'Player 1 will be playing with {playermarkerlist[0]}, while player 2 will be playing with {playermarkerlist[1]}.')
    time.sleep(5)
    return playermarkerlist

def player_input():
    # ask for the player's position. Keep asking if answer's out of bounds.
    while True:
        answer = int(input('Please enter a number for your position: '))
        if answer < 1 or answer > 9:
            print('Answer out of bounds. Try again.')
        else:
            break
    return answer

def space_check(board, position):
    # check if the position has white space. If whitespace, return True  
    return board[position] == ' '

def place_marker(board, marker, position):
    newboard = board
    
    # put the marker in the board
    newboard[position] = marker
    
    return newboard

def full_board_check(board):
    check = True
    
    # check if the board has any white space. if it does, the board isn't full and exits the loop automatically.
    for items in board:
        if items == ' ':
            check = False
            break
    
    return check

def win_check(board, mark):
    win = False
    # list the win conditions
    if board[1] == board[2] == board[3] and board[1] == mark and board[1] != ' ':
        win = True
    elif board[4] == board[5] == board[6] and board[4] == mark and board[4] != ' ':
        win = True
    elif board[7] == board[8] == board[9] and board[7] == mark and board[7] != ' ':
        win = True
    elif board[1] == board[4] == board[7] and board[1] == mark and board[1] != ' ':
        win = True
    elif board[2] == board[5] == board[8] and board[2] == mark and board[2] != ' ':
        win = True
    elif board[3] == board[6] == board[9] and board[3] == mark and board[3] != ' ':
        win = True
    elif board[1] == board[5] == board[9] and board[1] == mark and board[1] != ' ':
        win = True
    elif board[3] == board[5] == board[7] and board[3] == mark and board[3] != ' ':
        win = True
    
    # check win
    return win

def replay():
    while True:
        answer = input("Want to play again? Type 'yes' if you do. Type 'no' if you don't: ")
        if answer.lower() == 'yes':
            return True
            break
        elif answer.lower() == 'no':
            return False
            break
        else:
            print('Not a valid answer!')
                
# initialize the tic tac toe board. Once that's done, init will now be false
init = True

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    if init:
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        #use index to determine player
        playermark = ['', '']
        init = False
        playerturn = choose_first()
        
        #choose marker
        playermark = set_marker(playerturn)
    
    #while game_on, stops if the board is now full:
    while not full_board_check(board):
        display_board(board)    
        print(f"It's Player {playerturn + 1}'s turn!")
        position = player_input()
        
        # make sure the position chosen is empty
        while not space_check(board, position):
            print('Something is in that position. Try again.')
            position = player_input()
        board = place_marker(board, playermark[playerturn], position)
        
        # check if anyone wins
        if win_check(board, 'X') or win_check(board, 'O'):
            break
        
        #change players
        if playerturn == 0:
            playerturn = 1
        else:
            playerturn = 0
            
    display_board(board) 
    
    # check who won
    if win_check(board, 'X'):   # X wins
        if playermark[0] == 'X':
            print('Congratulations! Player 1 (X) won!')
        else:
            print('Congratulations! Player 2 (X) won!')
    elif win_check(board, 'O'): # O wins
        if playermark[0] == 'O':
            print('Congratulations! Player 1 (O) won!')
        else:
            print('Congratulations! Player 2 (O) won!')
    elif not win_check(board, 'X') and not win_check(board, 'O'):
        print("Looks like it's a tie")
            
    # end of game, ask to replay or not
    if replay():
        init = True
        print('Restarting the game...')
    else:
        print('Thank you for playing!')
        break
