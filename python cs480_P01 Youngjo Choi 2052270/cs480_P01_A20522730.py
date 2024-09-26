import sys
import game_A20522730
import state_A20522730
import tree_A20522730
import copy

# if wrong inputs are typed, error message will be printed
if len(sys.argv) != 4:  # Including the script name, we expect 4 arguments in total
    print("Error: Not enough / too many/ illegal input arguments")
    sys.exit(1)
elif sys.argv[1] != "1" and sys.argv[1] !=  "2":   # ALGO
   print("Error: Not enough / too many/ illegal input arguments")
   sys.exit(1)
elif sys.argv[2] != 'X' and sys.argv[2] != 'O': # FIRST
    print("Error: Not enough / too many/ illegal input arguments")
    sys.exit(1)
elif sys.argv[3] != "1" and sys.argv[3] != "2":   # MODE
    print("Error: Not enough / too many/ illegal input arguments")
    sys.exit(1)  # Exit the script with an error code

# Extract the arguments
file_name = sys.argv[0]
ALGO_name = None
Mode_name = None

if sys.argv[1] == "1":
    ALGO_name = "MiniMax"
elif sys.argv[1] == "2":
    ALGO_name = "MiniMax with alpha-beta pruning"

if sys.argv[3] == "1":
    Mode_name = "human versus computer"
elif sys.argv[3] == "2":
    Mode_name = "computer versus computer"

ALGO = sys.argv[1]  # string: either 1 or 2
FIRST = sys.argv[2] # string: either "X" or "O"
MODE = sys.argv[3]  # string: either "1" or "2"

print("Youngjo, Choi, A20522730 solution:")
print(f"Algorithm: {ALGO_name}")
print(f"FIRST: {FIRST}")
print(f"MODE: {Mode_name}")

# instantiate objects
game_obj = game_A20522730.Game(FIRST)
state_obj = state_A20522730.State()
tree_obj = tree_A20522730.Tree()
            
# mode_1: human(X) v. computer
def mode_1(state_obj, game_obj):
    #print(state_obj.board)
    game_obj.print_board(state_obj)
    while(not game_obj.is_terminal(state_obj)):
        if game_obj.to_move(state_obj) == "X":  # human's turn
            user_move = int(input(f"X's move. What is your move (possible moves at the moment are: {game_obj.actions(state_obj)} | enter 0 to exit the game)? "))
            if user_move == 0:
                exit()
            if user_move < 1 or user_move > 9 :
                continue    # go back to the while loop
            else:
                state_obj = game_obj.result(state_obj, user_move) 
                #print(state_obj.board)
                game_obj.print_board(state_obj)

        elif game_obj.to_move(state_obj) == "O":    # Computer's turn
            tree_obj.nodes_generated = 0
            if ALGO == "1": # minimax
                computer_move = tree_obj.minimax_search(game_obj, state_obj) 
            elif ALGO == "2":   # alpha-beta
               computer_move = tree_obj.alpha_beta_search(game_obj, state_obj)  
            state_obj = game_obj.result(state_obj, computer_move)  
            print(f"O's selected move: {computer_move}. Number of search tree nodes generated:{tree_obj.nodes_generated}")
            #print(state_obj.board)
            game_obj.print_board(state_obj)

    if game_obj.winner == "draw":
        print("TIE")
    elif game_obj.winner == "X":
        print("X WON")
    elif game_obj.winner == "O":
        print("O WON")
    
# mode_2: computer v. computer
def mode_2(state_obj, game_obj):
    #print(state_obj.board)
    game_obj.print_board(state_obj)
    while(not game_obj.is_terminal(state_obj)):
        if game_obj.to_move(state_obj) == "X":  
            tree_obj.nodes_generated = 0
            computer_move_X = tree_obj.minimax_search(game_obj, state_obj) 
            state_obj = game_obj.result(state_obj, computer_move_X)  
            print(f"X's selected move: {computer_move_X}. Number of search tree nodes generated:{tree_obj.nodes_generated}")
            #print(state_obj.board) 
            game_obj.print_board(state_obj)

        elif game_obj.to_move(state_obj) == "O":    # Computer's turn
            tree_obj.nodes_generated = 0
            computer_move_O = tree_obj.minimax_search(game_obj, state_obj) 
            state_obj = game_obj.result(state_obj, computer_move_O)  
            print(f"O's selected move: {computer_move_O}. Number of search tree nodes generated:{tree_obj.nodes_generated}")
            #print(state_obj.board)
            game_obj.print_board(state_obj)

    if game_obj.winner == "draw":
        print("TIE")
    elif game_obj.winner == "X":
        print("X WON")
    elif game_obj.winner == "O":
        print("O WON")

if MODE == "1": # human(X) v. computer(O)
    mode_1(state_obj, game_obj)
elif MODE == "2":   # computer(X) v. computer(O)
    mode_2(state_obj, game_obj)



