import encodeBits as bit
import os.path
import json
import random

MAX = 30000
MIN = -1

def findMinMax(minA,maxA,a):
    return min(minA,a),max(maxA,a)

def processData(fileName):

    data = []
    with open(fileName, "r") as f:
        data = f.readlines()
    
    minA2,minA3,minA8,minA11,minA14,minA15 = MAX,MAX,MAX,MAX,MAX,MAX
    maxA2,maxA3,maxA8,maxA11,maxA14,maxA15 = MIN,MIN,MIN,MIN,MIN,MIN
    processed = []

    for example in data:
        a1Value,a2Value,a3Value,a4Value,a5Value,a6Value,a7Value,a8Value,\
        a9Value,a10Value,a11Value,a12Value,a13Value,a14Value,a15Value,a16Value= example.split(",")

        a1,a3,a4,a5,a6,a7,a8=a1Value,float(a3Value),a4Value,a5Value,a6Value,a7Value,float(a8Value)
        a9,a10,a11,a12,a13,a14,a15,a16= a9Value,a10Value,int(a11Value),a12Value,a13Value,a14Value,int(a15Value),a16Value.rstrip()
        
        if (a2Value == "?"):
            a2 = a2Value
        else:
            a2 = float(a2Value)
            minA2,maxA2 = findMinMax(minA2,maxA2,a2)

        if (a14Value == "?"):
            a14 = a14Value
        else:
            a14 = int(a14Value)
            minA14,maxA14 = findMinMax(minA14,maxA14,a14)

        minA3,maxA3 = findMinMax(minA3,maxA3,a3)
        minA8,maxA8 = findMinMax(minA8,maxA8,a8)
        minA11,maxA11 = findMinMax(minA11,maxA11,a11)
        minA15,maxA15 = findMinMax(minA15,maxA15,a15)

        a = (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16)
        processed.append(a)

    return processed

def getData(fileName):

    rawData = processData(fileName)
    data = []

    for example in rawData:
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,c = example

        a1Bit = bit.getBitA1(a1)
        a2Bit = bit.getBitA2(a2)
        a3Bit = bit.getBitA3(a3)
        a4Bit = bit.getBitA4(a4)
        a5Bit = bit.getBitA5(a5)
        a6Bit = bit.getBitA6(a6)
        a7Bit = bit.getBitA7(a7)
        a8Bit = bit.getBitA8(a8)
        a9Bit = bit.getBitA9(a9)
        a10Bit = bit.getBitA10(a10)
        a11Bit = bit.getBitA11(a11)
        a12Bit = bit.getBitA12(a12)
        a13Bit = bit.getBitA13(a13)
        a14Bit = bit.getBitA14(a14)
        a15Bit = bit.getBitA15(a15)
        classBit = bit.getBitClass(c)

        individual = a1Bit+a2Bit+a3Bit+a4Bit+a5Bit+a6Bit+a7Bit+a8Bit+a9Bit+a10Bit+a11Bit+a12Bit+a13Bit+a14Bit+a15Bit+classBit


        dataBit = "".join(str(x) for x in individual)
    
        data.append(individual)

    return data


def chooseData(data):

    size = len(data)

    amountToChoose = size*0.7
    lst = []

    for i in range(0,int(amountToChoose)):
        index = random.randrange(0,size)
        example = data.pop(index)
        lst.append(example)
        size -= 1

    return lst, data


def saveData(train,test,extension):

    trainFile = "../data/train/"+extension
    testFile = "../data/test/"+extension

    with open(trainFile, mode='w') as f:
        json.dump(train,f)

    with open(testFile, mode='w') as f:
        json.dump(test,f)


def saveResults(file,result,correct,timestr):
    
    data = []

    if not os.path.isfile(file):
        with open(file, mode='w') as f:
            json.dump([], f)
            
    with open(file, mode='r') as f:
        data = json.load(f)

    with open(file, mode='w') as f:
        entry = {'time': timestr,'correct': correct,'hypothesis': result}
        data.append(entry)
        json.dump(data,f)


if __name__ == '__main__':
    data = processData("../data/crx.data")

    for example in data:

        for element in example:

            if element == "?":
                print example
                break

