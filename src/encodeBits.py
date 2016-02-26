
def getBitA1(a1):
    if (a1 == "b"):
        return [1,0]
    elif (a1 == "a"):
        return [0,1]
    else:
        return [1,1]

        # return [None]

def getBitA2(a2):
    if (a2 <= 20):
        return [1,0,0]
    elif (a2 <= 40):
        return [0,1,0]
    elif (a2 <= 81):
        return [0,0,1]
    else:
        return [1,1,1]
        # return [None]

def getBitA3(a3):
    if (a3 <= 0):
        return [1,0,0,0]
    elif (a3 <= 4):
        return [0,1,0,0]
    elif (a3 <= 7):
        return [0,0,1,0]
    elif (a3 <= 28):
        return [0,0,0,1]
    else:
        return [1,1,1,1]
        # return [None]

def getBitA4(a4):
    if (a4 == "u"):
        return [1,0,0,0]
    elif (a4 == "y"):
        return [0,1,0,0]
    elif (a4 == "l"):
        return [0,0,1,0]
    elif (a4 == "t"):
        return [0,0,0,1]
    else:
        return [1,1,1,1]
        # return [None]

def getBitA5(a5):
    if (a5 == "g"):
        return [1,0,0]
    elif (a5 == "p"):
        return [0,1,0]
    elif (a5 == "gg"):
        return [0,0,1]
    else:
        return [1,1,1]
        # return [None]

def getBitA6(a6):
    if (a6 == "c"):
        return [1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (a6 == "d"):
        return [0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (a6 == "cc"):
        return [0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif (a6 == "i"):
        return [0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif (a6 == "j"):
        return [0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif (a6 == "k"):
        return [0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif (a6 == "m"):
        return [0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif (a6 == "r"):
        return [0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif (a6 == "q"):
        return [0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif (a6 == "w"):
        return [0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    elif (a6 == "x"):
        return [0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif (a6 == "e"):
        return [0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif (a6 == "aa"):
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    elif (a6 == "ff"):
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    else:
        return [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        # return [None]

def getBitA7(a7):
    if (a7 == "v"):
        return [1,0,0,0,0,0,0,0,0]
    elif (a7 == "h"):
        return [0,1,0,0,0,0,0,0,0]
    elif (a7 == "bb"):
        return [0,0,1,0,0,0,0,0,0]
    elif (a7 == "j"):
        return [0,0,0,1,0,0,0,0,0]
    elif (a7 == "n"):
        return [0,0,0,0,1,0,0,0,0]
    elif (a7 == "z"):
        return [0,0,0,0,0,1,0,0,0]
    elif (a7 == "dd"):
        return [0,0,0,0,0,0,1,0,0]
    elif (a7 == "ff"):
        return [0,0,0,0,0,0,0,1,0]
    elif (a7 == "o"):
        return [0,0,0,0,0,0,0,0,1]
    else:
        return [1,1,1,1,1,1,1,1,1]
        return [None]

def getBitA8(a8):
    if (a8 <= 0):
        return [1,0,0]
    elif (a8 <= 2):
        return [0,1,0]
    elif (a8 <= 29):
        return [0,0,1]
    else:
        return [1,1,1]
        # return [None]    

def getBitA9(a9):
    if (a9 == "t"):
        return [1,0]
    elif (a9 == "f"):
        return [0,1]
    else:
        return [1,1]
        # return [None]

def getBitA10(a10):
    if (a10 == "t"):
        return [1,0]
    elif (a10 == "f"):
        return [0,1]
    else:
        return [1,1]
        # return [None]

def getBitA11(a11):
    if (a11 <= 0):
        return [1,0,0]
    elif (a11 <= 2):
        return [0,1,0]
    elif (a11 <= 67):
        return [0,0,1]
    else:
        return [1,1,1]
        # return [None]

def getBitA12(a12):
    if (a12 == "t"):
        return [1,0]
    elif (a12 == "f"):
        return [0,1]
    else:
        return [1,1]
        # return [None]

def getBitA13(a13):
    if (a13 == "g"):
        return [1,0,0]
    elif (a13 == "p"):
        return [0,1,0]
    elif (a13 == "s"):
        return [0,0,1]
    else:
        return [1,1,1]
        # return [None]

def getBitA14(a14):
    if (a14 <= 100):
        return [1,0,0]
    elif (a14 <= 200):
        return [0,1,0]
    elif (a14 <= 2000):
        return [0,0,1]
    else:
        return [1,1,1]
        # return [None]

def getBitA15(a15):
    if (a15 <= 0):
        return [1,0,0,0]
    elif (a15 <= 15):
        return [0,1,0,0]
    elif (a15 <= 500):
        return [0,0,1,0]
    elif (a15 <= 100000):
        return [0,0,0,1]
    else:
        return [1,1,1,1]
        # return [None]

def getBitClass(c):
    if (c == "+"):
        return [1]
    elif (c == "-"):
        return [0]
    else:
        return [1]
        # return [None]