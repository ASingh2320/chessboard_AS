class Piece:
    def __init__(self):
        self.moves = []
        self.ID = " "
        self.color = " "
        
    def setN(self):
        self.ID = "N"

    def setB(self):
        self.ID = "B"
        
    def setQ(self):
        self.ID = "Q"

    def setK(self):
        self.ID = "K"

    def setR(self):
        self.ID = "R"

    def setP(self):
        self.ID = "p"

    def getID(self):
        return self.ID;

    def getMoves(self):
        return self.moves

    def getSide(self):
        return self.color

    def setWh(self):
        self.color = "white"

    def setBl(self):
        self.color = "black"
        


