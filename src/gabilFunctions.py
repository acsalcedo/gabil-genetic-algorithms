from pyevolve import Util
import random

global dataSet

#List of the sizes of the atributes of each hypothesis/rule.
atributeSizes = [2,3,4,4,3,14,9,3,2,2,3,2,3,3,4]
RULESIZE = 62

#Sets data set.
def setDataSet(data):
    global dataSet
    dataSet = data

#Splits a set of hypotheses into a list of hypothesis.
def splitHypotheses(hypotheses):
    return [hypotheses[i:i+RULESIZE] for i in xrange(0, len(hypotheses),RULESIZE)]

#Verifies if the atribute of the hypothesis is more general than the rule.
def isMoreGeneral(atrHyp,atrRule):

    for i in range(len(atrHyp)):
        if atrHyp[i] != atrRule[i] and atrHyp[i] == 0:
            return False
    return True

#Verifies if a hypothesis matches with the rule.
def isMatch(hypothesis,rule):

    start = 0
    for size in atributeSizes:

        end = start+size
        atrHyp = hypothesis[start:end]
        atrRule = rule[start:end]

        compare =  isMoreGeneral(atrHyp,atrRule)

        if not compare:
            return False
        
        start += size 
    return True

#Verifies if the hypothesis and rule belong to the same class.
def isCorrectClass(hypothesis,rule):
    return hypothesis[61] == rule[61]

#Fitness function for an individual.
def fitness(chromosome):

    hypotheses = splitHypotheses(chromosome)
    score = 0.0
    correct = 0

    for rule in dataSet:
        
        for hypothesis in hypotheses:

            if isMatch(hypothesis,rule):

                if isCorrectClass(hypothesis,rule):
                    correct += 1
                    break
                else:
                    correct -= 1


    dataSetSize = len(dataSet)
    
    correct = correct / float(dataSetSize)
    score = correct * correct
    
    if correct < 0 or len(chromosome) > 62*20: # or len(chromosome) < 62*2:
        score = 0.0

    return score #/ float(len(chromosome)) 

#Verifies if a set of hypothesis classify correctly an example of the data set.
def classify(data,best):
    hypotheses = splitHypotheses(best)
    score = 0.0
    correct = 0
    
    for hypothesis in hypotheses:

        if isMatch(hypothesis,data):

            if isCorrectClass(hypothesis,data):
                return 1
            else:
                return 0 
    return 0 

#Calculates the number of examples correctly classified.
def correctlyClassified(best):

    correct = 0
    for example in dataSet:
        correct += classify(example,best)

    percentage = correct / float(len(dataSet))
    return correct, percentage*100

#Crossover function, using two point crossover.
def crossover(genome, **args):
    sister = None
    brother = None
    gMom = args["mom"]
    gDad = args["dad"]

    points = [random.randrange(0, (len(gMom))/ RULESIZE) , random.randrange(0, (len(gMom))/RULESIZE)]

    if points[0] > points[1]:
        Util.listSwapElement(points, 0, 1)

    remainder = [random.randrange(0, RULESIZE), random.randrange(0, RULESIZE)]

    if remainder[0] > remainder[1]:
        Util.listSwapElement(remainder, 0, 1)

    points2 = [random.randrange(0, len(gDad) / RULESIZE), random.randrange(0, len(gDad)/RULESIZE)]

    if points2[0] > points2[1]:
        Util.listSwapElement(points2, 0, 1)

    cut1 = points[0]*RULESIZE+remainder[0]
    cut2 = points[1]*RULESIZE+remainder[1]
    cut3 = points2[0]*RULESIZE+remainder[0]
    cut4 = points2[1]*RULESIZE+remainder[1]

    if args["count"] >= 1:
        sister = gMom.clone()
        sister.resetStats()
        sister[cut1:cut2] = gDad[cut3:cut4]
        sister.listSize = len(sister.genomeList)

    if args["count"] == 2:
        brother = gDad.clone()
        brother.resetStats()
        brother[cut3:cut4] = gMom[cut1:cut2]
        brother.listSize = len(brother.genomeList)

    return (sister, brother)
