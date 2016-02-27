from pyevolve import Util
import random

global dataSet
atributeSizes = [2,3,4,4,3,14,9,3,2,2,3,2,3,3,4,1]
RULESIZE = 62

def setDataSet(data):
    global dataSet
    dataSet = data

def splitHypotheses(hypotheses):
    return [hypotheses[i:i+RULESIZE] for i in xrange(0, len(hypotheses),RULESIZE)]

def moreGeneral(atrHyp,atrRule,lastAtribute):

    for i in range(len(atrHyp)):

        if atrHyp[i] == 1:

            if lastAtribute and atrHyp[i] != atrRule[i]:
                return False
            continue
        else:
            if atrRule[i] != 0:
                return False
    return True

def compareAtributes(hypothesis,rule):

    start = 0
    for size in atributeSizes:

        end = start+size
        atrHyp = hypothesis[start:end]
        atrRule = rule[start:end]
        lastAtribute = size == 1

        if not moreGeneral(atrHyp,atrRule,lastAtribute):
            return 1

        start += size 
    return 0

def fitnessFunction(chromosome):

    hypotheses = splitHypotheses(chromosome)
    wrongRules = 0
    score = 0.0

    for rule in dataSet:
        
        wrongHypothesis = 0
        
        for hypothesis in hypotheses:
            wrongHypothesis += compareAtributes(hypothesis,rule)
           
        if wrongHypothesis == len(hypotheses):
            wrongRules += 1

    dataSetSize = len(dataSet)
    rightRules = dataSetSize - wrongRules
    
    correct = rightRules / float(dataSetSize)
    score = correct * correct
    return score

def classify(data,best):

    hypotheses = splitHypotheses(best)
    wrongHypothesis = 0
        
    for hypothesis in hypotheses:
        wrongHypothesis += compareAtributes(hypothesis,data)

    if wrongHypothesis == len(hypotheses):
        return 0
    return 1

def crossover(genome, **args):
    sister = None
    brother = None
    gMom = args["mom"]
    gDad = args["dad"]
    RULESIZE = 62

    cuts = [random.randrange(0, (len(gMom))/ RULESIZE) , random.randrange(0, (len(gMom))/RULESIZE)]

    if cuts[0] > cuts[1]:
        Util.listSwapElement(cuts, 0, 1)

    remainder = [random.randrange(0, RULESIZE), random.randrange(0, RULESIZE)]

    if remainder[0] > remainder[1]:
        Util.listSwapElement(remainder, 0, 1)

    cuts2 = [random.randrange(0, len(gDad) / RULESIZE), random.randrange(0, len(gDad)/RULESIZE)]

    if cuts2[0] > cuts2[1]:
        Util.listSwapElement(cuts2, 0, 1)


    if args["count"] >= 1:
        sister = gMom.clone()
        sister.resetStats()
        sister[cuts[0]*RULESIZE+remainder[0]:cuts[1]*RULESIZE+remainder[1]] = \
        gDad[cuts2[0]*RULESIZE+remainder[0]:cuts2[1]*RULESIZE+remainder[1]]
        sister.listSize = len(sister.genomeList)

    if args["count"] == 2:
        brother = gDad.clone()
        brother.resetStats()
        brother[cuts2[0]*RULESIZE+remainder[0]:cuts2[1]*RULESIZE+remainder[1]] = \
        gMom[cuts[0]*RULESIZE+remainder[0]:cuts[1]*RULESIZE+remainder[1]]
        brother.listSize = len(brother.genomeList)

    return (sister, brother)

def calculateCorrect(best):

    correct = 0
    for example in dataSet:
        correct += classify(example,best)

    percentage = correct / float(len(dataSet))
    return percentage