from src.mars_rover import Rover
from src.classes_and_parser import Compass, InputParser

def test_rover_given_long_list_of_instructions():
    test_parser = InputParser()
    test_rover = Rover(1,2,Compass('N'))
    parsed_instructions = test_parser.parse_instruction('LMLMLMLMM')
    test_rover.move(parsed_instructions)
    assert test_rover.position.x == 1
    assert test_rover.position.y == 3
    assert test_rover.position.compass.name == 'NORTH'

def test_rover_given_long_list_of_instructions_2():
    test_parser = InputParser()
    test_rover = Rover(3,3,Compass('E'))
    parsed_instructions = test_parser.parse_instruction('MMRMMRMRRM')
    test_rover.move(parsed_instructions)
    assert test_rover.position.x == 5
    assert test_rover.position.y == 1
    assert test_rover.position.compass.name == 'EAST'