from functools import reduce

instruction_str = "R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2"

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

R = 1
L = -1

def full_instruction_str_to_array(full_inst_str):
    """
    >>> full_instruction_str_to_array("R5, R4, R2")
    ['R2', 'R4', 'R5']
    """
    return full_inst_str.replace(' ','').split(',')[::-1]

def instruction_str_to_tuple(inst):
    """
    >>> instruction_str_to_tuple('R5')
    (1, 5)
    >>> instruction_str_to_tuple('L199')
    (-1, 199)
    """
    return (eval(inst[0]), int(inst[1:]))

def move(turn_direction, move_distance, starting_direction=NORTH, starting_coord = [0,0]):
    """
    >>> move(R, 1)
    [1, [1, 0]]
    >>> move(R, 5, SOUTH, [10,10])
    [3, [5, 10]]
    """
    turn_direction = (starting_direction + turn_direction) % 4
    new_coord = calculate_new_coord(starting_coord, turn_direction, move_distance)
    # print("Now at {} facing {}".format(new_coord, turn_direction))
    return [turn_direction, new_coord]

def move2(inst_arr, direction=NORTH, coords = [0,0]):
    """
    >>> move2([(R, 1)])
    [1, 0]
    >>> move2([(L, 5)], NORTH, [0,0])
    [-5, 0]
    >>> move2([(L, 5), (L, 4)], NORTH, [0,0])
    [-4, -5]
    """
    # base case: inst_arr is empty, return current coordinates
    if len(inst_arr) == 0:
        return coords
    current_inst = inst_arr.pop() # yields like [-1, 5]
    new_direction = (direction + current_inst[0]) % 4
    move_distance = current_inst[1]
    print(coords, new_direction, move_distance)
    new_coords = calculate_new_coord(coords, new_direction, move_distance)
    # print("Now at {} facing {}".format(new_coords, new_direction))
    # new_direction, new_coords = map(lambda x: x[0] + direction, inst_arr.pop())
    return move2(inst_arr, new_direction, new_coords)


def calculate_new_coord(starting_coord, direction, distance):
    """
    >>> calculate_new_coord([0,0], NORTH, 1)
    [0, 1]
    >>> calculate_new_coord([10,10], WEST, 10)
    [0, 10]
    >>> calculate_new_coord([5,5], SOUTH, 10)
    [5, -5]
    >>> calculate_new_coord([0,0], 3, 5)
    [-5, 0]
    """
    # Which index is changing? Are we moving along x (index 0) or y (index 1)?
    coord_index = int(direction == NORTH or direction == SOUTH)
    # Are we moving in a positive or negative direction? By how much?
    coord_change = (1 + (-2) * int(direction == SOUTH or direction == WEST)) * distance
    # print("changing coord_index {} by {}".format(coord_index, coord_change))
    new_coord = starting_coord
    new_coord[coord_index] = starting_coord[coord_index] + coord_change
    # print(new_coord)
    return new_coord

def other_thing(inst_arr):
    """

    >>>
    """ 

def move_all(inst_arr):
    while len(inst_arr) > 0:
        turn, dist = inst_arr.pop()
        move

def apply_inst(init_coordir, inst):
    """
    >>> apply_inst([0,0,0], (1, 1))
    (1, 0, 1)
    >>> apply_inst([1,1,0], (1, 3))
    (4, 1, 1)
    >>> apply_inst([1,1,1], (1, 3))
    (1, -2, 2)
    >>> apply_inst([1,1,2], (1, 3))
    (-2, 1, 3)
    >>> apply_inst([1,1,3], (1, 3))
    (1, 4, 0)
    >>> apply_inst([5,5,3], (-1, 3))
    (5, 2, 2)
    """
    print("Currently at ({},{}) facing {}".format(init_coordir[0], init_coordir[1], init_coordir[2]) )
    new_direction = ( init_coordir[2] + inst[0] ) % 4 # direction facing
    # return (init_coordir[0] + ( -1 * (new_direction == WEST)  * (new_direction not in (NORTH, SOUTH)) * inst[1] , init_coordir[0] + ( -1 * (new_direction == SOUTH) * (new_direction not in (EAST, WEST))   * inst[1] , new_direction)
    new_coordir = (
        init_coordir[0] + ( 1 + -2 * (( init_coordir[2] + inst[0] ) % 4 == WEST) )  * (( init_coordir[2] + inst[0] ) % 4 not in (NORTH, SOUTH)) * inst[1] ,    # x coord
                         #  -1 * (1 if going west else 0) * ( 1 if traveling along x else 0) * distance          
        init_coordir[1] + ( 1 + -2 * (( init_coordir[2] + inst[0] ) % 4 == SOUTH) ) * (( init_coordir[2] + inst[0] ) % 4 not in (EAST, WEST))   * inst[1] ,    # y coord 
        ( init_coordir[2] + inst[0] ) % 4) # direction facing
    print("Moved {}, now at ({},{})".format(inst[1], new_coordir[0], new_coordir[1]) )
    return new_coordir

# print(sum([abs(x) for x in move2([instruction_str_to_tuple(inst_str) for inst_str in full_instruction_str_to_array(instruction_str) ], NORTH, [0,0])]))

def test():
    # instruction_str = "R5, L5, L5, L5"
    global instruction_str
    inst_arr = [(eval(inst[0]), int(inst[1:])) for inst in instruction_str.replace(' ','').split(',')] ## <<< currently, this looks like [(-1, 5), (1, 3), ...]
    # print (inst_arr)
    # we want to be able to use reduce() on this to turn it into our final coord
    print(sum([abs(x) for x in (reduce(lambda x, y: (
        x[0] + ( 1 + -2 * (( x[2] + y[0] ) % 4 == WEST) )  * (( x[2] + y[0] ) % 4 not in (NORTH, SOUTH)) * y[1] ,x[1] + ( 1 + -2 * (( x[2] + y[0] ) % 4 == SOUTH) ) * (( x[2] + y[0] ) % 4 not in (EAST, WEST))   * y[1] ,( x[2] + y[0] ) % 4), [(eval(inst[0]), int(inst[1:])) for inst in instruction_str.replace(' ','').split(',')], [0,0, NORTH] ))][:2]))


test()

# a, b = move(L, 10)
# move(L,10, a, b)

# if __name__ == "__main__":
#     import doctest
#     print = lambda *args, **kwargs: None
#     doctest.testmod()