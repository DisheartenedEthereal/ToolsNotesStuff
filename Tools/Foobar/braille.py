
def solution(plaintext):
    inp_splitted = list(plaintext)
    def replace_letter(text):

        def norm(txt):
            if txt == "a":
                return "100000"
            elif txt == " ":
                return "000000"
            elif txt == "b":
                return "110000"
            elif txt == "c":
                return "100100"
            elif txt == "d":
                return "100110"
            elif txt == "e":
                return "100010"
            elif txt == "f":
                return "110100"
            elif txt == "g":
                return "110110"
            elif txt == "h":
                return "110010"
            elif txt == "i":
                return "010100"
            elif txt == "j":
                return "010110"
            elif txt == "k":
                return "101000"
            elif txt == "l":
                return "111000"
            elif txt == "m":
                return "101100"
            elif txt == "n":
                return "101110"
            elif txt == "o":
                return "101010"
            elif txt == "p":
                return "111100"
            elif txt == "q":
                return "111110"
            elif txt == "r":
                return "111010"
            elif txt == "s":
                return "011100"
            elif txt == "t":
                return "011110"
            elif txt == "u":
                return "101001"
            elif txt == "v":
                return "111001"
            elif txt == "w":
                return "010111"
            elif txt == "x":
                return "101101"
            elif txt == "y":
                return "101111"
            elif txt == "z":
                return "101011"

            else:
                return "UNSUPPORTED"

        if text.isupper() == True:
            lowered = text.lower()
            return "000001" + norm(lowered)

        else: 
            return norm(text)

    plain = []
    for x in inp_splitted:
        
        plain.append(replace_letter(x))

        
    return''.join(plain)