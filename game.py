import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

from csquare import CSquare
    
class Game(CSquare):
    def __init__(self):
        self.board = [[CSquare(i,j) for i in range(8)]for j in range(8)]
        self.board[0][0].getPiece().setR()
        self.board[0][1].getPiece().setN()
        self.board[0][2].getPiece().setB()
        self.board[0][3].getPiece().setQ()
        self.board[0][4].getPiece().setK()
        self.board[0][5].getPiece().setB()
        self.board[0][6].getPiece().setN()
        self.board[0][7].getPiece().setR()
        for i in range(8):
            self.board[1][i].getPiece().setP()
        for i in range(2):
            for j in range(8):
                self.board[i][j].getPiece().setBl()

        self.board[7][0].getPiece().setR()
        self.board[7][1].getPiece().setN()
        self.board[7][2].getPiece().setB()
        self.board[7][3].getPiece().setQ()
        self.board[7][4].getPiece().setK()
        self.board[7][5].getPiece().setB()
        self.board[7][6].getPiece().setN()
        self.board[7][7].getPiece().setR()
        for i in range(8):
            self.board[6][i].getPiece().setP()
        for i in range(6,8):
            for j in range(8):
                self.board[i][j].getPiece().setWh()
    
    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board
        
    def printBoard(self):
        for i in range(8):
            for k in range(17):
                print("-", end = "")
            print()
            print("|", end = "")
            for j in range(8):
                if(self.board[i][j].getPiece().getSide() == "black"):
                    color.write(self.board[i][j].getPiece().getID(),"COMMENT")
                    print("|", end = "")
                    continue
                print(self.board[i][j].getPiece().getID() + "|", end = "")
            print(" " + str(8 - i), end = "")
            print()
        file = 'a'
        print(" ", end = "")
        for k in range (8):
            print(file + " ", end = "")
            file = chr(ord(file) + 1)
        print()
        
    def friendlyFire(self, moves, board, side):
        length = len(moves)
        moves3 = []
        for i in range(length):
            row = 8 - int(moves[i][1])
            col = ord(moves[i][0]) - 97
            if(board[row][col].getPiece().getSide() != side):
                moves3.append(moves[i])
        return moves3
    
    def getMoves(self, piece, rank, file, board):
        ID = piece.getID()
        moves = []
        if(ID == "N"):
            moves = []
            moves.append(chr(file + 97 - 2) + str(8 - rank + 1))
            moves.append(chr(file + 97 - 2) + str(8 - rank - 1))
            moves.append(chr(file + 97 - 1) + str(8 - rank + 2))
            moves.append(chr(file + 97 - 1) + str(8 - rank - 2))
            moves.append(chr(file + 97 + 1) + str(8 - rank + 2))
            moves.append(chr(file + 97 + 1) + str(8 - rank - 2))
            moves.append(chr(file + 97 + 2) + str(8 - rank + 1))
            moves.append(chr(file + 97 + 2) + str(8 - rank - 1))

            length = len(moves)
            moves2 = []

            for i in range(length):
                if(len(moves[i]) == 2 and moves[i][0] != "`" and int(moves[i][1]) < 9 and int(moves[i][1]) != 0 and moves[i][0] >= 'a' and moves[i][0] <= 'h'):
                    moves2.append(moves[i])
            side = piece.getSide()
            moves3 = self.friendlyFire(moves2, board, side)
            return moves3

        elif(ID == "B"):
            brank = rank
            bfile = file
            while(True):
                brank = brank + 1
                bfile = bfile + 1
                if(brank > 7 or bfile >7):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            
            brank = rank
            bfile = file
            while(True):
                brank = brank - 1
                bfile = bfile + 1
                if(brank < 0 or bfile > 7):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            brank = rank
            bfile = file
            while(True):
                brank = brank - 1
                bfile = bfile - 1
                if(brank < 0 or bfile < 0):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            brank = rank
            bfile = file
            while(True):
                brank = brank + 1
                bfile = bfile - 1
                if(brank > 7 or bfile < 0):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            return moves
        elif(ID == "R"):
            moves = []
            rrank = rank
            rfile = file
            while(True):
                rrank = rrank - 1
                if(rrank < 0):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)

            rrank = rank
            rfile = file
            while(True):
                rrank = rrank + 1
                if(rrank > 7):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)

            rrank = rank
            rfile = file
            while(True):
                rfile = rfile + 1
                if(rfile > 7):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)
            rrank = rank
            rfile = file
            while(True):
                rfile = rfile - 1
                if(rfile < 0):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)
            return moves
            
        elif(ID == "Q"):
            brank = rank
            bfile = file
            while(True):
                brank = brank + 1
                bfile = bfile + 1
                if(brank > 7 or bfile >7):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            
            brank = rank
            bfile = file
            while(True):
                brank = brank - 1
                bfile = bfile + 1
                if(brank < 0 or bfile > 7):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            brank = rank
            bfile = file
            while(True):
                brank = brank - 1
                bfile = bfile - 1
                if(brank < 0 or bfile < 0):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            brank = rank
            bfile = file
            while(True):
                brank = brank + 1
                bfile = bfile - 1
                if(brank > 7 or bfile < 0):
                    break
                if(board[brank][bfile].getPiece().getID() != " "):
                    if(board[brank][bfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(bfile + 97) + str(8 - brank)
                       moves.append(x)
                       break
                x = chr(bfile + 97) + str(8 - brank)
                moves.append(x)
            rrank = rank
            rfile = file
            while(True):
                rrank = rrank - 1
                if(rrank < 0):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)

            rrank = rank
            rfile = file
            while(True):
                rrank = rrank + 1
                if(rrank > 7):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)

            rrank = rank
            rfile = file
            while(True):
                rfile = rfile + 1
                if(rfile > 7):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)
            rrank = rank
            rfile = file
            while(True):
                rfile = rfile - 1
                if(rfile < 0):
                    break
                if(board[rrank][rfile].getPiece().getID() != " "):
                    if(board[rrank][rfile].getPiece().getSide() == piece.getSide()):
                        break;
                    else:
                       x = chr(rfile + 97) + str(8 - rrank)
                       moves.append(x)
                       break
                x = chr(rfile + 97) + str(8 - rrank)
                moves.append(x)
            return moves
        elif(ID == "K"):
            left = file - 1
            right = file + 1
            top = rank - 1
            bottom = rank + 1
            for i in range(top, bottom + 1):
                if(i < 0 or i > 7):
                    continue
                for j in range(left, right + 1):
                    if(i == rank and j == file):
                        continue
                    if(j < 0 or j > 7):
                        continue
                    moves.append(chr(j + 97) + str(8 - i))
            side = piece.getSide()
            moves = self.friendlyFire(moves, board, side)
            return moves
        elif(ID == "p"):
            side = piece.getSide()
            if(side == "black"):
                if(board[rank + 1][file].getPiece().getID() == " "):
                    moves.append(chr(file + 97) + str(8 - rank - 1))
                if(rank == 1 and board[rank + 2][file].getPiece().getID() == " "): 
                    moves.append(chr(file + 97) + str(8 - rank - 2))
                if(board[rank + 1][file - 1].getPiece().getID() != " " and board[rank + 1][file - 1].getPiece().getSide() == "white"):
                    moves.append(chr(file + 97 - 1) + str(8 - rank - 1))
                if(board[rank + 1][file + 1].getPiece().getID() != " " and board[rank + 1][file + 1].getPiece().getSide() == "white"):
                    moves.append(chr(file + 97 + 1) + str(8 - rank - 1))
            if(side == "white"):
                
                if(board[rank - 1][file].getPiece().getID() == " "):
                    moves.append(chr(file + 97) + str(8 - rank + 1))
                if(rank == 6 and board[rank - 2][file].getPiece().getID() == " "):
                    moves.append(chr(file + 97) + str(8 - rank + 2))
                if(board[rank - 1][file - 1].getPiece().getID() != " " and board[rank - 1][file - 1].getPiece().getSide() == "black"):
                    moves.append(chr(file + 97 - 1) + str(8 - rank + 1))
                if(board[rank - 1][file + 1].getPiece().getID() != " " and board[rank - 1][file + 1].getPiece().getSide() == "black"):
                    moves.append(chr(file + 97 + 1) + str(8 - rank + 1))
            return moves
    def isCheck(self, board, side):
        if(side == "white"):
            opside = "black"
        if(side == "black"):
            opside = "white"
        rank = -1
        file = -1
        for i in range (len(board)):
            for j in range (len(board[i])):
                if(board[i][j].getPiece().getID == "K" and board[i][j].getPiece().getSide() == opside):
                    rank = i
                    file = j
                    break
        kpos = chr(file + 97) + str(8 - rank)
        for i in range (len(board)):
            for j in range (len(board[i])):
                mov = board[i][j].getPiece().getMoves()
                for k in range (len(mov)):
                    if(mov[k] == kpos):
                        return True
        return False
            
        
                                


