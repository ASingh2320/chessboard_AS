from piece import Piece

class CSquare(Piece):
    def __init__(self, rank, file):
        self.piece = Piece()
        self.ID = chr(file + 97) + str(8 - rank)
        
    def Clear(self):
        self.piece = Piece()
    def getID(self):
        return self.ID
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def getRank(self):
        return self.rank
    def getFile(self):
        return self.file

        
