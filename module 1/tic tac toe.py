theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_kry=[]
for key in theBoard:
    board_kry.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn " + turn + ". Move to which place?")

        move = input()
         
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("The place is already occupied. Choose another place.")
            continue

        if count >= 5:
            if theBoard ['7']== theBoard ['8'] == theBoard ['9'] != ' ' :
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break
            elif theBoard ['4']== theBoard ['5'] == theBoard ['6'] != ' ' :
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break       
            elif theBoard ['1']== theBoard ['2'] == theBoard ['3'] != ' ' : 
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break   
            elif theBoard['1']== theBoard['4'] == theBoard['7'] != ' ':
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break
            elif theBoard['2']== theBoard['5'] == theBoard['8'] != ' ':
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break
            elif theBoard['3']== theBoard['6'] == theBoard['9'] != ' ':
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break
            elif theBoard['7']== theBoard['5'] == theBoard['3'] != ' ':
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break
            elif theBoard['1']== theBoard['5'] == theBoard['9'] != ' ':
                print(theBoard)
                print("\nGame Over.\n")
                print("****" + turn + " won the game! ****")
                break
        if  count == 9:
            print("\nGame Over.\n")
            print("It's a tie!")


        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play again? (yes/no): ")
    if    restart=="y"or restart=="Y":
        for key in board_kry:
            theBoard[key] = " "
        game()

if __name__ == "__main__":
    game()