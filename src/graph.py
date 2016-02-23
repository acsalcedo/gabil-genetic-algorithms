import matplotlib.pyplot as plt
import math
import numpy as np

def calculateRanges(data):

    ranges = [-1,100,200,2000]
    numRanges = len(ranges)
    rangePlus = []
    rangeNegative = []

    for i in range(numRanges):
        rangePlus.append(0)
        rangeNegative.append(0)

    for example in data:
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16 = example


        for i in range(len(ranges)):
            if (a14 <= ranges[i]):

                # To not add duplicates.
                if (a14 <= ranges[i-1] and ranges[i-1] < ranges[i]):
                    continue

                if (a16 == "+"):
                    rangePlus[i] += 1
                else:
                    rangeNegative[i] += 1                

    return rangePlus,rangeNegative

def graphRange(rangePlus,rangeNegative):

    ind = np.arange(len(rangePlus))
    width = 0.35  

    fig, ax = plt.subplots()
    barGraph = ax.bar(ind,rangePlus,width,color="g")
    barGraph2 = ax.bar(ind+width,rangeNegative,width,color="r")
    ax.set_xticks(ind + width)
    ax.set_xticklabels(("?", "[0,100]", "(100,200]", "(200,2000]"))
    ax.legend((barGraph[0],barGraph2[0]), ("+","-"),title="Clases")

    plt.xlabel("Rangos de Valores")
    plt.ylabel("Cantidad de Individuos")
    plt.title("Distribucion de Valores de A14")
    plt.grid(True)
    plt.savefig("../graphs/bargraph.png")