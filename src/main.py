from classes_and_parser import InputParser
from mars_rover import Rover

def main():
    
    parser = InputParser()
    number_of_rovers = input('number of rovers: ')
    inputs = input() + '\n'
    for _ in range(int(number_of_rovers)):
        inputs += input() + '\n'
        inputs += input() + '\n'
    inputs = inputs.split('\n')
    # print(inputs)
    inputs.pop()
    # print(inputs)
    plateau_size = parser.parse_plateau(inputs[0])

    # print((len(inputs)-1)/2)
    for i in range(int((len(inputs) - 1)/2)):
        # print(i)
        instructions = parser.parse_instruction(inputs[2 + (2*i)])
        rover_i_position = parser.parse_rover_position(inputs[(2*i)+1])
        rover_i = Rover(rover_i_position, plateau_size.x, plateau_size.y)
        rover_i.move(instructions)
        print(rover_i.position.x, rover_i.position.y, rover_i.position.compass.value)
    # rover1 = Rover(rover_position, plateau_size.x, plateau_size.y)
    # rover2 = Rover
    # print()
    # print(rover_position.__getattribute__('x'))
    # print(rover_position.__getattribute__('y'))
    # print(rover_position.__getattribute__('compass'))
    # print(plateau_size, rover_position)
    pass

main()