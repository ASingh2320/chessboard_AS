
from game import Game

checkmate = False
turn = "white"
play = Game()

while(checkmate != True):
    print("\n")
    board = play.getBoard()
    play.printBoard()
    print("Turn: " + turn)
    valin = False
    while(valin != True):
        pos = input("Select a piece by entering its position: ")
        if(len(pos) != 2 or (pos[0] < 'a' or pos[0] > 'h') or (int(pos[1]) < 1 or int(pos[1]) > 8)):
           print("This is not a valid position.")
           continue
        rank = 8 - int(pos[1])
        file = ord(pos[0]) - 97
        if(board[rank][file].getPiece().getSide() != turn):
            print("This is not a valid position.")
            continue
        valin = True
    piece = board[rank][file].getPiece()
    while(True):
        choice = input("a) See possible moves\n" + "b) Make move\n" + "Select next option: ")
        if(choice == "a" or choice == "A"):
            print(play.getMoves(piece, rank, file, board))
            break
        if(choice == "b" or choice == "B"):
            legal = play.getMoves(piece, rank, file, board)
            if(len(legal) == 0):
                print("This piece has no available moves")
                break
            valin = False
            while(valin == False):
                mov = input("Please enter move: ")
                found = False
                for i in range(len(legal)):
                    if(mov == legal[i]):
                        valin = True
                        break
            mrank = 8 - int(mov[1])
            mfile = ord(mov[0]) - 97
            board[mrank][mfile].setPiece(piece)
            board[rank][file].Clear()
            play.setBoard(board)
            if(turn == "white"):
                turn = "black"
            elif(turn == "black"):
                turn = "white"
            break
        print("Please enter a valid option.")
    
        
        
    
              
