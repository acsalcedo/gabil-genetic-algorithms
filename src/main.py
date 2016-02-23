from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Statistics
from pyevolve import DBAdapters
import pyevolve
import matplotlib.pyplot as plt
import math
import numpy as np

MAX = 30000
MIN = -1

def fitnessFunction():

    pass
    #fitness - (correct)**2

def findMinMax(minA,maxA,a):
    return min(minA,a),max(maxA,a)


def readFile(fileName):

    lines = []
    with open(fileName, "r") as f:
        lines = f.readlines()
    return lines

def processData(data):

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
        # minA14,maxA14 = findMinMax(minA14,maxA14,a14)
        minA15,maxA15 = findMinMax(minA15,maxA15,a15)

        a = (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16)
        # print a15
        processed.append(a)

    # print "Min2: %s Max2: %s, Min3: %s Max3: %s, Min8: %s Max8: %s, Min11: %s Max11: %s, Min14: %s Max14: %s, Min15: %s Max15: %s"  \
    # %(minA2,maxA2,minA3,maxA3,minA8,maxA8,minA11,maxA11,minA14,maxA14,minA15,maxA15)
    return processed


def main():

    fileData = readFile("../data/crx.data")

    data = processData(fileData)

    rangePlus,rangeNegative = calculateRanges(data)
    graphRange(rangePlus,rangeNegative)


def calculateRanges(data):

    numRanges = 2
    rangePlus = []
    rangeNegative = []

    for i in range(numRanges):
        rangePlus.append(0)
        rangeNegative.append(0)

    for example in data:
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16 = example


        if (a15 < 20):
            if (a16 == "+"):
                rangePlus[0] += 1
            else:
                rangeNegative[0] += 1

        elif (a15 <= 100000):
            if (a16 == "+"):
                rangePlus[1] += 1
            else:
                rangeNegative[1] += 1

    return rangePlus,rangeNegative

def graphRange(rangePlus,rangeNegative):

    # print rangeList
    ind = np.arange(2)
    width = 0.35  

    fig, ax = plt.subplots()
    barGraph = ax.bar(ind,rangePlus,width,color="g")
    barGraph2 = ax.bar(ind+width,rangeNegative,width,color="r")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('R1', 'R2'))
    ax.legend((barGraph[0],barGraph2[0]), ("+","-"))
    # for i in ind:
        # print ind
        # print rangePlus[i]
    # plt.xlabel('Neuronas')
    # plt.ylabel('Error')ist
    # plt.title('Error de la Clasificacion de Datos')
    # plt.grid(True)
    plt.savefig("bargraph.png")



if __name__ == '__main__':
    main()