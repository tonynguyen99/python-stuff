class Robot:
    def __init__(self, name, colour, weight):
        self.name = name
        self.colour = colour
        self.weight = weight
    
    def introduce_self(self):
        print("My name is %s, I am %s and I am %s" % (self.name, self.colour, self.weight))


class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        
        
    def sit_down(self):
        self.is_sitting = True
    
    
    def stand_up(self):
        self.is_sitting = False