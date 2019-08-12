from dice import D20

class Hand(list):
    def __init__(self, size = 0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        for _ in range(size):
            self.append(die_class()) 
        
    @property
    def total(self):
        return sum(self)
    
    def roll(rolls):
        return Hand(size=rolls, die_class=D20)