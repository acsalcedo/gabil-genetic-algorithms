
def setBitA1(a1):
    if (a1 == [1,0]):
        return ["b"]
    elif (a1 == [0,1]):
        return ["a"]
    else:
        return ["?"]

def setBitA2(a2):
    if (a2 <= [1,0,0]):
        return [20]
    elif (a2 <= [0,1,0]):
        return [40]
    elif (a2 <= [0,0,1]):
        return [81]
    else:
        return ["?"]

def setBitA3(a3):
    if (a3 == [1,0,0,0]):
        return [0]
    elif (a3 == [0,1,0,0]):
        return [4]
    elif (a3 == [0,0,1,0]):
        return [7]
    elif (a3 == [0,0,0,1]):
        return [28]
    else:
        return ["?"]

def setBitA4(a4):
    if (a4 == [1,0,0,0]):
        return ["u"]
    elif (a4 == [0,1,0,0]):
        return ["y"]
    elif (a4 == [0,0,1,0]):
        return ["l"]
    elif (a4 == [0,0,0,1]):
        return ["t"]
    else:
        return ["?"]

def setBitA5(a5):
    if (a5 == [1,0,0]):
        return ["g"]
    elif (a5 == [0,1,0]):
        return ["p"]
    elif (a5 == [0,0,1]):
        return ["gg"]
    else:
        return ["?"]

def setBitA6(a6):
    if (a6 == [1,0,0,0,0,0,0,0,0,0,0,0,0,0]):
        return ["c"]
    elif (a6 == [0,1,0,0,0,0,0,0,0,0,0,0,0,0]):
        return ["d"]
    elif (a6 == [0,0,1,0,0,0,0,0,0,0,0,0,0,0]):
        return ["cc"]
    elif (a6 == [0,0,0,1,0,0,0,0,0,0,0,0,0,0]):
        return ["i"]
    elif (a6 == [0,0,0,0,1,0,0,0,0,0,0,0,0,0]):
        return ["j"]
    elif (a6 == [0,0,0,0,0,1,0,0,0,0,0,0,0,0]):
        return ["k"]
    elif (a6 == [0,0,0,0,0,0,1,0,0,0,0,0,0,0]):
        return ["m"]
    elif (a6 == [0,0,0,0,0,0,0,1,0,0,0,0,0,0]):
        return ["r"]
    elif (a6 == [0,0,0,0,0,0,0,0,1,0,0,0,0,0]):
        return ["q"]
    elif (a6 == [0,0,0,0,0,0,0,0,0,1,0,0,0,0]):
        return ["w"]
    elif (a6 == [0,0,0,0,0,0,0,0,0,0,1,0,0,0]):
        return ["x"]
    elif (a6 == [0,0,0,0,0,0,0,0,0,0,0,1,0,0]):
        return ["e"]
    elif (a6 == [0,0,0,0,0,0,0,0,0,0,0,0,1,0]):
        return ["aa"]
    elif (a6 == [0,0,0,0,0,0,0,0,0,0,0,0,0,1]):
        return ["ff"]
    else:
        return ["?"]

def setBitA7(a7):
    if (a7 == [1,0,0,0,0,0,0,0,0]):
        return ["v"]
    elif (a7 == [0,1,0,0,0,0,0,0,0]):
        return ["h"]
    elif (a7 == [0,0,1,0,0,0,0,0,0]):
        return ["bb"]
    elif (a7 == [0,0,0,1,0,0,0,0,0]):
        return ["j"]
    elif (a7 == [0,0,0,0,1,0,0,0,0]):
        return ["n"]
    elif (a7 == [0,0,0,0,0,1,0,0,0]):
        return ["z"]
    elif (a7 == [0,0,0,0,0,0,1,0,0]):
        return ["dd"]
    elif (a7 == [0,0,0,0,0,0,0,1,0]):
        return ["ff"]
    elif (a7 == [0,0,0,0,0,0,0,0,1]):
        return ["o"]
    else:
        return ["?"]

def setBitA8(a8):
    if (a8 == [1,0,0]):
        return [0]
    elif (a8 == [0,1,0]):
        return [2]
    elif (a8 == [0,0,1]):
        return [29]
    else:
        return ["?"]    

def setBitA9(a9):
    if (a9 == [1,0]):
        return ["t"]
    elif (a9 == [0,1]):
        return ["f"]
    else:
        return ["?"]

def setBitA10(a10):
    if (a10 == [1,0]):
        return ["t"]
    elif (a10 == [0,1]):
        return ["f"]
    else:
        return ["?"]

def setBitA11(a11):
    if (a11 == [1,0,0]):
        return [0]
    elif (a11 == [0,1,0]):
        return [2]
    elif (a11 == [0,0,1]):
        return [67]
    else:
        return ["?"]

def setBitA12(a12):
    if (a12 == [1,0]):
        return ["t"]
    elif (a12 == [0,1]):
        return ["f"]
    else:
        return ["?"]

def setBitA13(a13):
    if (a13 == [1,0,0]):
        return ["gg"]
    elif (a13 == [0,1,0]):
        return ["p"]
    elif (a13 == [0,0,1]):
        return ["s"]
    else:
        return ["?"]

def setBitA14(a14):
    if (a14 == [1,0,0]):
        return [100]
    elif (a14 == [0,1,0]):
        return [200]
    elif (a14 == [0,0,1]):
        return [2000]
    else:
        return ["?"]

def setBitA15(a15):
    if (a15 == [1,0,0,0]):
        return [0]
    elif (a15 == [0,1,0,0]):
        return [15]
    elif (a15 == [0,0,1,0]):
        return [500]
    elif (a15 == [0,0,0,1]):
        return [100000]
    else:
        return ["?"]

def setBitClass(c):
    if (c == [1]):
        return ["+"]
    elif (c == [0]):
        return ["-"]
    else:
        return ["?"]
