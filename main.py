import random

is_running = True
count = 0
value = 9

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
map = [row1, row2, row3]

def player_play():
    global is_running
    while is_running:
        flag = 0

        try:
            move = int(input("Choose the number from ( 1 - 9 ) :"))
        except ValueError:
            print("Wrong selection, Choose again!!")
        else:
            for i in map:
                for j in range(0, 3):
                    if move == i[j]:
                        flag = 1
                        i[j] = player_choice
                        computer_play()
                    else:
                        pass
            if flag == 0:
                print("Already chosen, Choose again!!")


def computer_play():
    global value
    while True:
        computer_row = random.randint(0, 2)
        computer_col = random.randint(0, 2)

        print("\nYour Play:")
        win_or_loose()

        if map[computer_row][computer_col] == player_choice or map[computer_row][computer_col] == computer_choice:
            print("Computer choosing again")
            value+=1
        else:
            map[computer_row][computer_col] = computer_choice
            print("\nComputer Play:")
            win_or_loose()
            break


def win_or_loose():
    global is_running
    global count
    print(f"{row1}\n{row2}\n{row3}")

    if computer_choice == 'X':
        if row1 == ['X', 'X', 'X'] or row2 == ['X', 'X', 'X'] or row3 == ['X', 'X', 'X']:
            print("Computer Win!!!")
            exit()
        elif row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X' or row1[1] == 'X' and row2[1] == 'X' and row3[
            1] == 'X' or row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
            print("Computer Win!!!")
            exit()
        elif row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X' or row1[2] == 'X' and row2[1] == 'X' and row3[
            0] == 'X':
            print("Computer Win!!!")
            exit()


    elif computer_choice == 'O':
        if row1 == ['O', 'O', 'O'] or row2 == ['O', 'O', 'O'] or row3 == ['O', 'O', 'O']:
            print("Computer Win!!!")
            exit()
        elif row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O' or row1[1] == 'O' and row2[1] == 'O' and row3[
            1] == 'O' or row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
            print("Computer Win!!!")
            exit()
        elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O' or row1[2] == 'O' and row2[1] == 'O' and row3[
            0] == 'O':
            print("Computer Win!!!")
            exit()


    if player_choice == 'X':
        if row1 == ['X', 'X', 'X'] or row2 == ['X', 'X', 'X'] or row3 == ['X', 'X', 'X']:
            print("Player Win!!!")
            exit()
        elif row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X' or row1[1] == 'X' and row2[1] == 'X' and row3[
            1] == 'X' or row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X':
            print("Player Win!!!")
            exit()
        elif row1[0] == 'X' and row2[1] == 'X' and row3[2] == 'X' or row1[2] == 'X' and row2[1] == 'X' and row3[
            0] == 'X':
            print("Player Win!!!")
            exit()

    elif player_choice == 'O':
        if row1 == ['O', 'O', 'O'] or row2 == ['O', 'O', 'O'] or row3 == ['O', 'O', 'O']:
            print("Player Win!!!")
            exit()
        elif row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O' or row1[1] == 'O' and row2[1] == 'O' and row3[
            1] == 'O' or row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O':
            print("Player Win!!!")
            exit()
        elif row1[0] == 'O' and row2[1] == 'O' and row3[2] == 'O' or row1[2] == 'O' and row2[1] == 'O' and row3[
            0] == 'O':
            print("Player Win!!!")
            exit()

    count += 1
    # print(f"count {count}")
    # print(f"value {value}")
    if count == value:
        print("Draw Match")
        exit()


while True:
    while True:
        player_choice = input("Choose your symbol ( X or O ) : ").upper()
        computer_choice = ""
        print(player_choice)
        if player_choice != "X" and player_choice != "O":
            print("Wrong option, Choose again!!")
            break
        elif player_choice == "X":
            computer_choice = "O"
        else:
            computer_choice = "X"

        print(f"Player symbol: {player_choice}")
        print(f"Computer symbol: {computer_choice}")
        print(f"{row1}\n{row2}\n{row3}")
        player_play()








