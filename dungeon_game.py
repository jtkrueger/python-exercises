import random


matrix = []
x_grid = []
y_grid = []

def map_size():
    while True:
        x_grid = input('How many spaces wide is your dungeon?')
        y_grid = input('How many spaces tall is your dungeon?')
    
        try:
            x_int = int(x_grid)
        except:
            print("Spaces must be a whole number")
            continue
        try:
            y_int = int(y_grid)
        except:
            print("Spaces must be a whole number")
            continue
        if x_int < 1 or y_int < 1:
            print("Spaces must be greater than 1")
            continue
        else:
            break
    
    x_grid = range(x_int)
    y_grid = range(y_int)
    for y in y_grid:
        for x in x_grid:
            matrix.append((x, y))
    return x_grid, y_grid


def get_locations():
    monster = random.choice(matrix)
    door = random.choice(matrix)
    player = random.choice(matrix)

    if monster == player or monster == door or player == door:
        return get_locations()

    return monster, door, player


def move_player(player, move):
    # player = (x, y)
    x, y = player

    if move == 'LEFT':
        x -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'UP':
        y -= 1
    elif move == 'DOWN':
        y += 1

    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    # player = (x, y)
    if player[0] == 0:
        moves.remove('LEFT')
    if player[0] == len(x_grid) - 1:
        moves.remove('RIGHT')
    if player[1] == 0:
        moves.remove('UP')
    if player[1] == len(y_grid) - 1:
        moves.remove('DOWN')

    return moves


def draw_map(player):
    tile = '|{}'
    for x in x_grid:
        print(' _', end='')
    print(' ')

    # The index of left coordinates in the map grid 
    left_coords = []
    for y in y_grid:
        y = y * len(x_grid)
        for x in x_grid:
            if x == len(x_grid) - 1:
                pass
            else:
                left_coords.append(x + y)           

    for index, cell in enumerate(matrix):
        if index in left_coords:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))
        

x_grid, y_grid = map_size()
monster, door, player = get_locations()
print("Welcome to the dungeon!")

while True:
    moves = get_moves(player)
    print("You're currently in room {}".format(player))

    draw_map(player)
    
    print("You can move {}".format(moves)) 
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("** Walls are hard. Stop walking into them! **")
        continue

    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the grue!")
        break


    
