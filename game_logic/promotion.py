def want_and_able_to_promote(pieceName, piecePos, color, promotion):
    if promotion == "P": # check if is already promoted
        promotion = True
    else:
        promotion = False
    if pieceName.lower()[1:] != "king" and pieceName.lower()[1:] != "gold" and not promotion:
        if color == "white":
            print(piecePos)
            if piecePos <= 2: # check if is able to promo
                
                x = input(f"Do you want to promote your {pieceName}? (y/n) ").lower() == "y"
                if x:
                    print("Promoted")
                    return True
        elif color == "black":
            print(piecePos)
            if piecePos >= 6: # check if is able to promo
                x = input("Do you want to promote your {pieceName}? (y/n) ").lower() == "y"
                if x:
                    print("Promoted")
                    return True
        else:
            return False
    else :
        return False