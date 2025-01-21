

captured_by_white = {}
counter = 1  # Licznik, który będzie używany jako klucz w słowniku
for i in range(8, 0, -1):
    captured_by_white[counter] = {"pos": (i, 0), "piece": None}
    counter += 1  # Zwiększamy licznik
    captured_by_white[counter] = {"pos": (i, 1), "piece": None}
    counter += 1
    captured_by_white[counter] = {"pos": (i, 2), "piece": None}
    counter += 1

captured_by_black = {}
counter = 1  # Licznik, który będzie używany jako klucz w słowniku
for i in range(8, 0, -1):
    captured_by_black[counter] = {"pos": (i, 12), "piece": None}
    counter += 1
    captured_by_black[counter] = {"pos": (i, 13), "piece": None}
    counter += 1
    captured_by_black[counter] = {"pos": (i, 14), "piece": None}
    counter += 1


def capture_piece(piece):
        if piece[0] == "w":  
            piece_to_capture = "b" + piece[1:]
            piece_to_capture = f"{piece_to_capture.split('_')[0]}_NPY"
            for key, value in captured_by_black.items():
                if value["piece"] is None: 
                    value["piece"] = piece_to_capture
                    break
        elif piece[0] == "b":
            piece_to_capture = "w" + piece[1:]
            piece_to_capture = f"{piece_to_capture.split('_')[0]}_NPY"
            for key, value in captured_by_white.items():
                if value["piece"] is None:  
                    value["piece"] = piece_to_capture  
                    break
        print("Captured by White:")
        for key, value in captured_by_white.items():
            print(f"Pos: {value['pos']}, Piece: {value['piece']}")
        print("Captured by Black:")
        for key, value in captured_by_black.items():
            print(f"Pos: {value['pos']}, Piece: {value['piece']}")  

def del_from_dict(color, start_pos):
    if color == "black":
        for key, value in captured_by_black.items():
            if value["pos"] == start_pos:
                value["piece"] = None
                break
    elif color == "white":
        for key, value in captured_by_white.items():
            if value["pos"] == start_pos:
                value["piece"] = None
                break

def get_captured_by_white():
        return captured_by_white

def get_captured_by_black():
        return captured_by_black
