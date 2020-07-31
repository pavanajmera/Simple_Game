
list = [0,1,2,3,4,5,6,7,8,9]

def dispaly_game(list):
    print("Hey! Here is the list which we have \n ")
    print(list,"\n")
dispaly_game(list)

def positon_choice():
    choice = "WRONG"
    acceptable_range = [0,1,2,3,4,5,6,7,8,9]
    within_range = False
    choice  = input("Enter your index between(0-9): ")
    if choice.isdigit() == True:
         if int(choice) in acceptable_range:
            within_range = True
         else:
            print("TRY AGAIN")
            within_range = False
    return int(choice)
positon_choice()

def replace_choice(list,position):
    user_replace = input("Type a string or number to replace at position: ")
    list[position] = user_replace
    print(list,"\n")
    return list
replace_choice(list,0)

def select_choice():
    choice = "WRONG"
    while choice not in ['Y', 'N']:
        choice = input("If you need to continue GAME(Y or N): " )
        if choice not in ['Y', 'N']:
            print("Hey,Please choose correct option Yes or NO")

        if choice == 'Yes':
            return True
        else:
            return False
select_choice()

game_play = True
list = [0,1,2,3,4,5,6,7,8,9]
while game_play:
    dispaly_game(list)
    position = positon_choice()
    list = replace_choice(list,position)
    dispaly_game(list)
    game_play = select_choice()
