from gabilFunctions import setDataSet, calculateCorrect, fitnessFunction2, fitnessFunction, crossover, CrossoverDeGabil, CrossoverTwoPoint
from pyevolve import GSimpleGA, G1DList, Selectors, Statistics, Crossovers, G1DBinaryString
from G1DListModified import G1DListModified
from processData import getData
import matplotlib.pyplot as plt
import sys, os.path,getopt
import numpy as np
import pyevolve

dataFolder = "../data/"

def printError():
    print "\n$ python main.py -f <inputFile> -p <selectionTypeParents> -s <selectionTypeSurvivors> -m <mutationRate> -c <crossoverRate> -x <penalization>"
    print "\nType of Parent Selection or Survivor Selection:"
    print "\t1 -> Roulette Wheel"
    print "\t2 -> Tournament Selector"
    print "\nPenalization:"
    print "\t0 -> No penalization"
    print "\t1 -> Penalization"
    print "All parameters are optional except the input file."
    print
    sys.exit(2)

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"f:p:s:m:c:x:",["file=","parents=","survivors=","mutation=","crossover=","penalization="])
    except getopt.GetoptError:
        print "\nIncorrect call. Please try again."
        printError()

    inputFile = None
    parentSelection,survivorSelection = 1,1
    mutationRate,crossoverRate = 0.02,0.8
    penalize = False
    
    for opt, arg in opts:

        if opt in ("-f", "--file"):
            inputFile = str(arg)
        if opt in ("-p", "--parents"):
            parentSelection = int(arg)
        elif opt in ("-s", "--survivors"):
            survivorSelection = int(arg)
        elif opt in ("-m", "--mutation"):
            mutationRate = float(arg)
        elif opt in ("-c", "--crossover"):
            crossoverRate = float(arg)
        elif opt in ("-x", "--penalization"):
            if (int(arg) == 1):
                penalize = True

    if inputFile is None:
        print "\nPlease enter an input file."
        printError()
        sys.exit()

    filePath = dataFolder+inputFile

    if not os.path.isfile(filePath):
        print "\nThe file '%s' does not exist.\n" %(filePath)
        sys.exit()

    #Set size of individual
    # genome = G1DBinaryString.G1DBinaryString(62*2)
    # genome = G1DListModified(62)
    genome = G1DList.G1DList(62)

    #Set range of elements in the list of the invidividual
    genome.setParams(rangemin=0, rangemax=1)

    #Reads rules from file
    data = getData(filePath)

    # print data

    setDataSet(data)
    ga = GSimpleGA.GSimpleGA(genome,seed=39)
    genome.evaluator.set(fitnessFunction2) 

    if (parentSelection == 1):
        ga.selector.set(Selectors.GRouletteWheel)
    else:
        ga.selector.set(Selectors.GTournamentSelector)

    ga.setGenerations(5000)
    ga.setPopulationSize(20)
    ga.setMutationRate(mutationRate)
    ga.setCrossoverRate(crossoverRate)
    ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)

    # genome.crossover.set(Crossovers.G1DBinaryStringXTwoPoint)
    # genome.crossover.set(Crossovers.G1DListCrossoverTwoPoint)
    # genome.crossover.set(CrossoverTwoPoint)
    genome.crossover.set(CrossoverDeGabil)

    ga.evolve(freq_stats=20)

    best = ga.bestIndividual()
    print best

    print "Percentage: %s" %(calculateCorrect(best))

if __name__ == '__main__':
    main(sys.argv[1:])