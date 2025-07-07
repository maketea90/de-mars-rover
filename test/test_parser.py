from src.classes_and_parser import InputParser, Instruction, Compass, Position
import pytest

def test_input_parser_given_string_parses_instructions():
    test_parser = InputParser()
    instruction = test_parser.parse_instruction('LRMR')
    assert [instruction[0].name, instruction[1].name, instruction[2].name, instruction[3].name] == ['LEFT', 'RIGHT', 'MOVE', 'RIGHT']
    
    with pytest.raises(ValueError):
        test_parser.parse_instruction('RLMRLMRLMas;dofji[dsasdfoji902LASDOFOIADSFMSDAFR]')

def test_input_parser_parses_coordinates():
    parser = InputParser()
    plateau = parser.parse_plateau('55')
    assert (plateau.x, plateau.y) == (5,5)
    with pytest.raises(ValueError):
        parser.parse_plateau('1234mfsdadfdask')

def test_input_parser_given_string_parses_coordinates():
    test_parser = InputParser()
    rover_position = test_parser.parse_rover_position('12N') 
    assert [rover_position.x, rover_position.y, rover_position.compass.name] == [1,2,'NORTH']
    with pytest.raises(ValueError):
        test_parser.parse_rover_position('23Nasdflkm')
