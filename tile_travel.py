# 1  make variables for the directions and x, y coordinates
# 2  find out out which direction he can take
# 3  ask which for direction input
# 4  move the player
# 5  if the player is on tile 3, 1 the player wins 
# 6  else continue

# Variables
NORTH = "n"
SOUTH = "s"
EAST = "e"
WEST = "w"
X = 1
Y = 1

# Functions

def move_options(x,y):
    ''' Function which tells which direction you can move
    input: position of player, x and y
    output: 4 boolean values for all directions in addition with count of True values'''

    n_bool, s_bool, e_bool, w_bool = True, True, True, True
    option_count = 4  # Number of True booleans
    # These conditions tell wether you can move to certain directions
    if(x == 1 or (y==1) or (x==3 and y==2)):  # West
        w_bool = False
        option_count -= 1
    if(x == 3 or (y==1) or (x==2 and y==2)):  # East
        e_bool = False
        option_count -= 1
    if(y==3 or (x==2 and y==2)):              # North
        n_bool = False
        option_count -= 1
    if(y==1 or (x==2 and y==3)):              # South
        s_bool = False
        option_count -= 1

    return n_bool, e_bool, s_bool, w_bool, option_count
        

def print_options(n,e,s,w, count):
    ''' Function that prints out the options for the player
    input: booleans and count from the move_options function, which directions you can move
    output: None, however prints available directions'''

    print("You can travel: ",end="")
    # If boolean is true and it is not the final direction, add or inbetween
    if(n and count != 1):             # North
        print("(N)orth", end=" or ")
        count -= 1
    # Else if its the final direction, add a dot instead
    elif (n and count == 1):
        print("(N)orth.")
        return None

    if(e and count != 1):             # East
        print("(E)ast", end=" or ")
        count -= 1
    elif (e and count == 1):
        print("(E)ast.")
        return None

    if(s and count != 1):             # South
        print("(S)outh", end=" or ")
        count -= 1
    elif (s and count == 1):
        print("(S)outh.")
        return None

    if(w and count != 1):             # West
        print("(W)est", end=" or ")
        count -= 1
    elif (w and count == 1):
        print("(W)est.")
        return None

#TODO:
# Make a function that moves the player
def move_player(x, y, move):
    ''' Function that changes the player position
    input: x and y position and user input for direction
    output: new x or y position'''
    if move == NORTH:
        y +=1
    elif move == SOUTH:
        y -= 1
    elif move == WEST:
        x -= 1
    elif move == EAST:
        x += 1
    return x, y

#TODO:
# Ask for input and save it
while True:  # The main loop
    n,e,s,w,count = move_options(X,Y)  # Assign booleans and count from possible direction options
    print_options(n,e,s,w,count)       # Print the options
    while True:
        # Get the input, if the input matches the boolean of the direction then break out, else ask for the input again
        input_str = input("Direction: ").lower()
        if((input_str == NORTH and n) or (input_str == EAST and e) or (input_str == SOUTH and s) or (input_str == WEST and w)):
            break
        else:
            print("Not a valid direction!")
            continue
    X,Y = move_player(X,Y,input_str)  # New position
    if X == 3 and Y == 1:  # If the player is on tile (3,1), then you win
        print("Victory!")
        break