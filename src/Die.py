import random

class Die:
    def __init__(self):
        self.faceValue = 0
        
    def roll(self):
        self.faceValue = random.randint(1,5)
        
    def getFaceValue(self):
        return self.faceValue
        
        