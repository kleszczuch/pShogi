def want_and_able_to_promote(pieceName, piecePos, color, promotion):
    if promotion == "P":
        promotion = True
    else:
        promotion = False
    if pieceName.lower()[1:] != "king" and pieceName.lower()[1:] != "gold" and not promotion:
        if color == "white":
            print(piecePos)
            if piecePos <= 2:
                
                x = input(f"Do you want to promote your {pieceName}? (y/n) ").lower() == "y"
                if x:
                    print("Promoted")
                    return True
        elif color == "black":
            print(piecePos)
            if piecePos >= 6:
                x = input("Do you want to promote your {pieceName}? (y/n) ").lower() == "y"
                if x:
                    print("Promoted")
                    return True
        else:
            return False
    else :
        return False