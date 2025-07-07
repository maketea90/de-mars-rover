from src.classes_and_parser import Position, Compass

class Rover:
    def __init__(self, position, plateau_size_x, plateau_size_y):
        self.position = position
        self.max_x = plateau_size_x
        self.max_y = plateau_size_y

    def move(self, instructions):
        for move in instructions:
            if self.position.compass.name == 'NORTH':
                if move.name == 'LEFT':
                    self.position.compass = Compass('W')
                elif move.name == 'RIGHT':
                    self.position.compass = Compass('E')
                else:
                    if self.position.y != self.max_y:
                        self.position.y += 1
            elif self.position.compass.name == 'EAST':
                if move.name == 'LEFT':
                    self.position.compass = Compass('N')
                elif move.name == 'RIGHT':
                    self.position.compass = Compass('S')
                else:
                    if self.position.x != self.max_x:
                        self.position.x += 1
            elif self.position.compass.name == 'SOUTH':
                if move.name == 'LEFT':
                    self.position.compass = Compass('E')
                elif move.name == 'RIGHT':
                    self.position.compass = Compass('W')
                else:
                    if self.position.y != 0:
                        self.position.y -= 1
            else:
                if move.name == 'LEFT':
                    self.position.compass = Compass('S')
                elif move.name == 'RIGHT':
                    self.position.compass = Compass('N')
                else:
                    if self.position.x != 0:
                        self.position.x -= 1
    
    # def has_rover_hit_edge_of_plateau(self):
    #     if self.position.x == 0