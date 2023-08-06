class Square:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name
    
    def __str__(self):
        return "Square: " + self.name