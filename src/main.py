from gabilFunctions import setDataSet, correctlyClassified, fitness, crossover
from G1DListModified import G1DListModified
from pyevolve import GSimpleGA, Selectors
from processData import getData, saveResults
import sys, os.path, getopt
import pyevolve

dataFolder = "../data/"
testFolder = "../tests/"

def printError():
    print "\n$ python main.py -f <inputFile> -p <selectionTypeParents> -s <selectionTypeSurvivors> ",
    print "-m <mutationRate> -c <crossoverRate> -x <penalization> -g <generations> -n <populationSize>"
    print "\nType of Parent Selection:"
    print "\t1 -> Roulette Wheel"
    print "\t2 -> Rank Selector"
    print "\t3 -> Tournament Selector"
    print "\nType of Survivor Selection:"
    print "\t0 -> No Elitism"
    print "\t1 -> Elitism"
    print "\nPenalization:"
    print "\t0 -> No penalization"
    print "\t1 -> Penalization"
    print "All parameters are optional except the input file."
    print
    sys.exit(2)

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"f:p:s:m:c:x:g:n:",["file=","parents=", \
            "survivors=","mutation=","crossover=","penalization=","generations=","population="])
    except getopt.GetoptError:
        print "\nIncorrect call. Please try again."
        printError()

    parentSelection,survivorSelection = 1,0
    mutationRate,crossoverRate = 0.02,0.8
    numGenerations = 1500
    inputFile = None
    penalize = False
    population = 20
    
    for opt, arg in opts:

        try: 
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
            elif opt in ("-g", "--generations"):
                numGenerations = int(arg)
            elif opt in ("-n", "--population"):
                population = int(arg)
        except ValueError:
            pass


    if inputFile is None:
        print "\nPlease enter an input file."
        printError()
        sys.exit()

    filePath = dataFolder+inputFile

    if not os.path.isfile(filePath):
        print "\nThe file '%s' does not exist.\n" %(filePath)
        sys.exit()

    genome = G1DListModified(62*8) #Set size of individual

    #Set range of elements in the list of the invidividual
    genome.setParams(rangemin=0, rangemax=1)

    genome.evaluator.set(fitness)
    genome.crossover.set(crossover)

    #Reads rules from file
    data = getData(filePath)
    setDataSet(data)

    ga = GSimpleGA.GSimpleGA(genome)
    # ga = GSimpleGA.GSimpleGA(genome,seed=39)
    ga.setGenerations(numGenerations)
    ga.setPopulationSize(population)
    ga.setMutationRate(mutationRate)
    ga.setCrossoverRate(crossoverRate)
    # ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
    
    print "------------------------ SETTINGS FOR GABIL ------------------------"
    print "Crossover Rate: %s" %(crossoverRate)
    print "Mutation Rate: %s" %(mutationRate)
    print "Population Size: %s" %(population)
    print "Number of Generations: %s" %(numGenerations)

    if (parentSelection == 1):
        ga.selector.set(Selectors.GRouletteWheel)
        print "Parent Selection: Roulette Wheel."
    elif (parentSelection == 2):
        ga.selector.set(Selectors.GRankSelector)        
        print "Parent Selection: Rank."
    else:
        ga.selector.set(Selectors.GTournamentSelector)
        print "Parent Selection: Tournament."

    if (survivorSelection == 1):
        ga.setElitism(True)
        print "Survivor Selection: Elitism is set."
    else:
        print "Survivor Selection: Elitism is not set."

    print "--------------------------------------------------------------------"

    ga.evolve(freq_stats=20)

    best = ga.bestIndividual()
    print "------------------ BEST INDIVIDUAL IN POPULATION -------------------\n%" 
    print best,
    print "--------------------------------------------------------------------"

    correct, percentage = correctlyClassified(best)
    print "Number of examples correctly classified: %s, Percentage: %s" %(correct,percentage)

    testFile = testFolder+"cross"+str(crossoverRate)+"_mut"+str(mutationRate) \
    + "_par"+str(parentSelection)+"_surv"+str(survivorSelection)+"_pop"+str(population) \
    + "_gen"+str(numGenerations)

    saveResults(testFile,best.genomeList,correct)



    # with open(testFile, mode='r') as f:
    #     data = json.load(f)
    #     avg = 0
    #     for example in data:
    #         avg += example['correct']

    #     print avg

if __name__ == '__main__':
    main(sys.argv[1:])