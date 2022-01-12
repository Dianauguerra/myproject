
row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]


player1 = "x"
player2 = "o"


def main():
    
    while True:
            
        print_answer()
        x_turn = int(input("x's turn to choose a square(1-9): "))
        get_answer(x_turn, player1)
        print_answer()

        if  row1[0] == row1[1] == row1[2] == player1 or \
            row2[0] == row2[1] == row2[2] == player1 or \
            row3[0] == row3[1] == row3[2] == player1 or \
            row1[0] == row2[1] == row3[2] == player1 or \
            row1[2] == row2[1] == row3[0] == player1 or \
            row3[0] == row3[1] == row3[2] == player1 or \
            row1[0] == row2[0] == row3[0] == player1 or \
            row1[1] == row2[1] == row3[1] == player1 or \
            row3[2] == row3[2] == row3[2] == player1:
            has_winner(player1)
            break
        
        o_turn = int(input("o's turn to choose a square(1-9): "))
        get_answer(o_turn, player2)
        print_answer()

        if  row1[0] == row1[1] == row1[2] == player2 or \
            row2[0] == row2[1] == row2[2] == player2 or \
            row3[0] == row3[1] == row3[2] == player2 or \
            row1[0] == row2[1] == row3[2] == player2 or \
            row1[2] == row2[1] == row3[0] == player2 or \
            row3[0] == row3[1] == row3[2] == player2 or \
            row1[0] == row2[0] == row3[0] == player2 or \
            row1[1] == row2[1] == row3[1] == player2 or \
            row3[2] == row3[2] == row3[2] == player2:
            has_winner(player2)
            break
        
    print("Game over. Try again.")
        

def get_answer(answer, player):

    if answer == 1:
        row1[0] = player
    elif answer == 2:
        row1[1] = player
    elif answer == 3:
        row1[2] = player
    elif answer == 4:
        row2[0] = player
    elif answer == 5:
        row2[1] = player
    elif answer == 6:
        row2[2] = player
    elif answer == 7:
        row3[0] = player
    elif answer == 8:
        row3[1] = player
    elif answer == 9:
        row3[2] = player
    else:
        print("Try again")
    
def print_answer():

    print()
    print(f"{row1[0]}|{row1[1]}|{row1[2]}")
    print('-+-+-')
    print(f"{row2[0]}|{row2[1]}|{row2[2]}")
    print('-+-+-')
    print(f"{row3[0]}|{row3[1]}|{row3[2]}")
    print()
    

def has_winner(player):
    print(f"Player {player} is the winner!")
    print_answer()
    


main()