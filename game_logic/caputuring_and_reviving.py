

captured_by_white = {}
counter = 1  # Licznik, który będzie używany jako klucz w słowniku
for i in range(8, 0, -1):
    captured_by_white[counter] = {"pos": (0, i), "piece": None}
    counter += 1  # Zwiększamy licznik
    captured_by_white[counter] = {"pos": (1, i), "piece": None}
    counter += 1
    captured_by_white[counter] = {"pos": (2, i), "piece": None}
    counter += 1

captured_by_black = {}
counter = 1  # Licznik, który będzie używany jako klucz w słowniku
for i in range(8, 0, -1):
    captured_by_black[counter] = {"pos": (12, i), "piece": None}
    counter += 1
    captured_by_black[counter] = {"pos": (13, i), "piece": None}
    counter += 1
    captured_by_black[counter] = {"pos": (14, i), "piece": None}
    counter += 1


def capture_piece(piece):
        if piece[0] == "w":  
            piece_to_capture = "b" + piece[1:]
            for key, value in captured_by_black.items():
                if value["piece"] is None: 
                    value["piece"] = piece_to_capture
                    break
        elif piece[0] == "b":
            piece_to_capture = "w" + piece[1:]
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


def get_captured_by_white():
        return captured_by_white

def get_captured_by_black():
        return captured_by_black
