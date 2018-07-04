t = [1,2,3,4,5,6,7,8,9]

#assign players to variable
player1_sym = "X"
player2_sym = "O"

#function to check for winner
def check_winner():
    #check for horizontal
    if t[0] == t[1] == t[2]:
        return True
    if t[3] == t[4] == t[5]:
        return True
    if t[6] == t[7] == t[8]:
        return True
    
    #check for vertical
    if t[0] == t[3] == t[6]:
        return True
    if t[1] == t[4] == t[7]:
        return True
    if t[2] == t[5] == t[8]:
        return True
    
    #check for diagonal
    if t[0] == t[4] == t[8]:
        return True
    if t[2] == t[4] == t[6]:
        return True

#function to display board
def display_board():
    print("\n")
    print(t[0],"\t",t[1],"\t",t[2],)
    print("----------------------")
    print(t[3],"\t",t[4],"\t",t[5],)
    print("----------------------")
    print(t[6],"\t",t[7],"\t",t[8],"\n")


display_board()

for d in range(1,10):

    if d % 2 == 0:
        for i in range(40):

            str_pos = input("\nPLAYER TWO CHOOSE A POSITION == ")            

            #if position is not a number
            if str_pos.isdigit() == False:
                print("\n!!!!!!!!!!! PLEASE INSERT A NUMBER !!!!!!!!!!!")
                display_board()
                continue
            else:
                pos = int(str_pos)

            #if position is greater than 9
            if pos > 9:
                print("\n!!!!!!!!!!!  PLEASE SELECT A NUMBER IN RANGE 1 - 9 !!!!!!!!!!!")
                display_board()
                continue

            #if position is occupied
            str_list = str(t[pos - 1])

            if str_list.isdigit() ==  False:
                print("\n!!!!!!!!!!!  PLEASE SELECT A VACANT POSITION !!!!!!!!!!!")
                display_board()
                continue

            #if no error condition is met
            t[pos-1] = player2_sym
            display_board()
            
            break
        
        if check_winner() == True:
                print("\n \n*********   PLAYER TWO WINS   ***********")
                break

    else:
        for i in range(40):
            str_pos = input("\nPLAYER ONE CHOOSE A POSITION == ")            

            #if position is not a number
            if str_pos.isdigit() == False:
                print("\n!!!!!!!!!!! PLEASE INSERT A NUMBER !!!!!!!!!!!")
                continue
            else:
                pos = int(str_pos)

            #if position is greater than 9
            if pos > 9:
                print("\n!!!!!!!!!!!  PLEASE SELECT A NUMBER IN RANGE 1 - 9 !!!!!!!!!!!")
                continue

            #if position is occupied
            str_list = str(t[pos - 1])

            if str_list.isdigit() ==  False:
                print("\n!!!!!!!!!!!  PLEASE SELECT A VACANT POSITION !!!!!!!!!!!")
                continue

            #if no error condition is met
            t[pos-1] = player1_sym
            display_board()
            
            break
        if check_winner() == True:
                print("\n \n*********   PLAYER ONE WINS   ***********")
                break

#if nobody wins
if check_winner() != True:

    print("!!!!!!!!! IT'S A TIE !!!!!!!!!!!!")
    print("!!!!!!!!! NOBODY WON !!!!!!!!!!!!")

