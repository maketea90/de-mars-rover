# upper_right_coordinates = input('Upper right coordinates (size of plateau): ')
# upper_right_coordinates = (int(str(upper_right_coordinates)[0]), int(str(upper_right_coordinates)[1]))
# print(upper_right_coordinates)
# lower_left_coordinates = (0,0)


# starting_position = input('Rover starting position: ')
# # starting_position = (int(str(starting_position)[0]), int(str(starting_position)[1]))
# print(starting_position)

from enum import Enum

class Instruction(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'

class Compass(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

class Position:
    def __init__(self,x,y,compass):
        self.x = x
        self.y = y
        self.compass = compass

class PlateauSize:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class InputParser:
    def __init__(self):

        pass

    def parse_instruction(self, instruction_str):
        parsed = []
        for c in instruction_str:
            parsed.append(Instruction(c))
        return parsed
        
    def parse_plateau(self, input):
        # try:
        if len(input) != 2:
            raise ValueError('MUST BE TWO NUMBERS')
        try:
            parsed = PlateauSize(int(input[0]), int(input[1]))
        except:
            raise ValueError('MUST BE TWO NUMBERS')
        return parsed
    
    def parse_rover_position(self, input):
        if len(input) != 3:
            raise ValueError('MUST BE TWO NUMBERS FOLLOWED BY A COMPASS DIRECTION')
        try:
            parsed = Position(int(input[0]), int(input[1]), Compass(input[2]))
        except ValueError:
            raise ValueError('MUST BE TWO NUMBERS FOLLOWED BY A COMPASS DIRECTION')
        return parsed