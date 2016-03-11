RULESIZE = 62


def setBitA1(a1):
    if (a1 == [1,0]):
        return ["b"]
    elif (a1 == [0,1]):
        return ["a"]
    elif (a1 == [1,1]):
        return ["a || b"]
    else:
        return ["?"]

def setBitA2(a2):
    if (a2 == [1,0,0]):
        return [20]
    elif (a2 == [0,1,0]):
        return [40]
    elif (a2 == [0,0,1]):
        return [81]
    elif (a2 == [1,1,0]):
        return ["20 || 40"]
    elif (a2 == [1,0,1]):
        return ["20 || 81"]
    elif (a2 == [0,1,1]):
        return ["40 || 81"]
    elif (a2 == [1,1,1]):
        return ["20 || 40 || 81"]
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
    elif (a3 == [1,1,0,0]):
	return ["0 || 4"]
    elif (a3 == [1,0,1,0]):
	return ["0 || 7"]
    elif (a3 == [1,0,0,1]):
	return ["0 || 28"]
    elif (a3 == [0,1,1,0]):
	return ["4 || 7"]
    elif (a3 == [0,1,0,1]):
	return ["4 || 28"]
    elif (a3 == [0,0,1,1]):
	return ["7 || 28"]
    elif (a3 == [1,1,1,0]):
	return ["0 || 4 || 7"]
    elif (a3 == [1,1,0,1]):
	return ["0 || 4 || 28"]
    elif (a3 == [1,0,1,1]):
	return ["0 || 7 || 28"]
    elif (a3 == [0,1,1,1]):
	return ["4 || 7 || 28"]
    elif (a3 == [1,1,1,1]):
	return ["0 || 4 || 7 || 28"]
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
    elif (a4 == [1,1,0,0]):
	return ["u || y"]
    elif (a4 == [1,0,1,0]):
	return ["u || l"]
    elif (a4 == [1,0,0,1]):
	return ["u || t"]
    elif (a4 == [0,1,1,0]):
	return ["y || l"]
    elif (a4 == [0,1,0,1]):
	return ["y || t"]
    elif (a4 == [0,0,1,1]):
	return ["l || t"]
    elif (a4 == [1,1,1,0]):
	return ["u || y || l"]
    elif (a4 == [1,1,0,1]):
	return ["u || y || t"]
    elif (a4 == [1,0,1,1]):
	return ["u || l || l"]
    elif (a4 == [0,1,1,1]):
	return ["y || l || t"]
    elif (a4 == [1,1,1,1]):
	return ["u || y || l || t"]
    else:
        return ["?"]

def setBitA5(a5):
    if (a5 == [1,0,0]):
        return ["g"]
    elif (a5 == [0,1,0]):
        return ["p"]
    elif (a5 == [0,0,1]):
        return ["gg"]
    elif (a5 == [1,0,1]):
        return ["g || gg"]
    elif (a5 == [1,1,0]):
        return ["g || p"]
    elif (a5 == [0,1,1]):
        return ["p || gg"]
    elif (a5 == [1,1,1]):
        return ["g || p || gg"]
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
    elif (a6 == [1,1,1,1,1,1,1,1,1,1,1,1,1,1]):
        return ["c || d || cc || i || j || k || m || r || q || w || x || e || aa || ff"]
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
    elif (a7 == [1,1,1,1,1,1,1,1,1]):
        return ["v || h || bb || n || z || dd || ff || o"]
    else:
        return ["?"]

def setBitA8(a8):
    if (a8 == [1,0,0]):
        return [0]
    elif (a8 == [0,1,0]):
        return [2]
    elif (a8 == [0,0,1]):
        return [29]
    elif (a8 == [1,1,0]):
        return ["0 || 2"]
    elif (a8 == [1,0,1]):
        return ["0 || 29"]
    elif (a8 == [0,1,1]):
        return ["2 || 29"]
    elif (a8 == [1,1,1]):
        return ["0 || 2 || 29"]
    else:
        return ["?"]    

def setBitA9(a9):
    if (a9 == [1,0]):
        return ["t"]
    elif (a9 == [0,1]):
        return ["f"]
    elif (a9 == [1,1]):
        return ["t || f"]
    else:
        return ["?"]

def setBitA10(a10):
    if (a10 == [1,0]):
        return ["t"]
    elif (a10 == [0,1]):
        return ["f"]
    elif (a10 == [1,1]):
        return ["t || f"]
    else:
        return ["?"]

def setBitA11(a11):
    if (a11 == [1,0,0]):
        return [0]
    elif (a11 == [0,1,0]):
        return [2]
    elif (a11 == [0,0,1]):
        return [67]
    elif (a11 == [1,1,0]):
        return ["0 || 2"]
    elif (a11 == [1,0,1]):
        return ["0 || 6"]
    elif (a11 == [0,1,1]):
        return ["2 || 6"]
    elif (a11 == [1,1,1]):
        return ["0 || 2 || 67"]
    else:
        return ["?"]

def setBitA12(a12):
    if (a12 == [1,0]):
        return ["t"]
    elif (a12 == [0,1]):
        return ["f"]
    elif (a12 == [1,1]):
        return ["t || f"]
    else:
        return ["?"]

def setBitA13(a13):
    if (a13 == [1,0,0]):
        return ["gg"]
    elif (a13 == [0,1,0]):
        return ["p"]
    elif (a13 == [0,0,1]):
        return ["s"]
    elif (a13 == [1,1,0]):
        return ["gg || p"]
    elif (a13 == [1,0,1]):
        return ["gg || s"]
    elif (a13 == [0,1,1]):
        return ["p || p"]
    elif (a13 == [1,1,1]):
        return ["gg || p || s"]
    else:
        return ["?"]

def setBitA14(a14):
    if (a14 == [1,0,0]):
        return [100]
    elif (a14 == [0,1,0]):
        return [200]
    elif (a14 == [0,0,1]):
        return [2000]
    elif (a14 == [1,0,1]):
        return ["100 || 2000"]
    elif (a14 == [1,1,0]):
        return ["100 || 200"]
    elif (a14 == [0,1,1]):
        return ["200 || 2000"]
    elif (a14 == [1,1,1]):
        return ["100 || 200 || 2000"]
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
    elif (a15 == [1,1,0,0]):
        return ["0 || 15"]
    elif (a15 == [1,0,1,0]):
        return ["0 || 500"]
    elif (a15 == [1,0,0,1]):
        return ["0 || 100000"]
    elif (a15 == [0,1,1,0]):
        return ["15 || 500"]
    elif (a15 == [0,1,0,1]):
        return ["15 || 100000"]
    elif (a15 == [0,0,1,1]):
        return ["50 || 100000"]
    elif (a15 == [1,1,1,0]):
        return ["0 || 15 || 500"]
    elif (a15 == [1,1,0,1]):
        return ["0 || 15 || 100000"]
    elif (a15 == [1,0,1,1]):
        return ["0 || 50 || 100000"]
    elif (a15 == [0,1,1,1]):
        return ["15 || 50 || 100000"]
    elif (a15 == [1,1,1,1]):
        return ["0 || 15 || 500 || 100000"]
    else:
        return ["?"]

def setBitClass(c):
    if (c == [1]):
        return ["+"]
    elif (c == [0]):
        return ["-"]
    else:
        return ["?"]

def splitHypotheses(hypotheses):
    return [hypotheses[i:i+RULESIZE] for i in xrange(0, len(hypotheses),RULESIZE)]

def printDecoded(hypotheses):
	for x in splitHypotheses(hypotheses):
		#print x
		print setBitA1(x[0:2]) + setBitA2(x[2:5]) + setBitA3(x[5:9]) + setBitA4(x[9:13]) + setBitA5(x[13:16]) + setBitA6(x[16:30]) + setBitA7(x[30:39]) + setBitA8(x[39:42]) + setBitA9(x[42:44]) + setBitA10(x[44:46]) + setBitA11(x[46:49]) + setBitA12(x[49:51]) + setBitA13(x[51:54]) + setBitA14(x[54:57]) + setBitA15(x[57:61])

individuo = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]
individuo2 = [0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,
1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,
1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,
0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,
0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,
1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,
1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,
1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,
0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,
1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,
1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,
0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,
1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,
1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,1,
1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,0,0,
0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,
1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1]
print len(individuo2) / 62
printDecoded(individuo2)
	
