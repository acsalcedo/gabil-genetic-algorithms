from random import randint as rand_randint
from pyevolve import Util
import random

global dataSet
atributeSizes = [2,3,4,4,3,14,9,3,2,2,3,2,3,3,4,1]
RULESIZE = 62

def setDataSet(data):
    global dataSet
    dataSet = data

def splitHypotheses(hypotheses):

    lst = [hypotheses[i:i+RULESIZE] for i in xrange(0, len(hypotheses),RULESIZE)]
    
    # lst2 = []
    # for l in lst: lst2.append("".join(str(x) for x in l))

    return lst

def moreGeneral(atrHyp,atrRule,lastAtribute):

    for i in range(len(atrHyp)):

        # print "hyp: %s rule: %s compare: %s" %(atrHyp[i], atrRule[i], (atrHyp[i] == 0))
        if (atrHyp[i] != atrRule[i]) and (lastAtribute or atrHyp[i] == str(0)):
            return False
    return True

def compareAtributes(hypothesis,rule):

    start = 0
    for size in atributeSizes:

        end = start+size
        atrHyp = hypothesis[start:end]
        atrRule = rule[start:end]

        lastAtribute = size == 1
        compare =  moreGeneral(atrHyp,atrRule,lastAtribute)
        # print "hyp: %s rule: %s compare: %s" %(atrHyp, atrRule, compare)

        if not compare:

            if lastAtribute:
                return 1

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
           
        if wrongHypothesis >= len(hypotheses):
            wrongRules += 1

    dataSetSize = len(dataSet)
    rightRules = dataSetSize - wrongRules
    
    correct = rightRules / float(dataSetSize)
    score = correct * correct
    return score #/float(len(chromosome))


def match(hypothesis,rule):

    start = 0
    for size in atributeSizes:

        end = start+size
        atrHyp = hypothesis[start:end]
        atrRule = rule[start:end]

        lastAtribute = size == 1
        compare =  moreGeneral(atrHyp,atrRule,lastAtribute)

        if not compare:
            return False
        
        start += size 
    return True

def correctClass(hypothesis,rule):

    return hypothesis[61] == rule[61]


def fitnessFunction2(chromosome):

    hypotheses = splitHypotheses(chromosome)
    score = 0.0
    correct = 0

    for rule in dataSet:
        
        for hypothesis in hypotheses:

            if match(hypothesis,rule):

                if correctClass(hypothesis,rule):
                    correct += 1
                else:
                    correct -= 1


    dataSetSize = len(dataSet)
    
    correct = correct / float(dataSetSize)
    score = correct * correct
    return score / float(len(chromosome))

def classify(data,best):

    hypotheses = splitHypotheses(best)
    wrongHypothesis = 0
        
    for hypothesis in hypotheses:

        wrongHypothesis += compareAtributes(hypothesis,data)

    if wrongHypothesis >= len(hypotheses):
        return 0
    return 1

def classify2(data,best):
    hypotheses = splitHypotheses(best)
    score = 0.0
    correct = 0
    
    for hypothesis in hypotheses:

        if match(hypothesis,data):

            if correctClass(hypothesis,data):
                return 1
            else:
                return 0
        else:
            return 0


def calculateCorrect(best):

    correct = 0
    for example in dataSet:
        correct += classify2(example,best)

    percentage = correct / float(len(dataSet))
    return percentage*100


def crossover(genome, **args):
    sister = None
    brother = None
    gMom = args["mom"]
    gDad = args["dad"]

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

        print sister.listSize

    if args["count"] == 2:
        brother = gDad.clone()
        brother.resetStats()
        brother[cuts2[0]*RULESIZE+remainder[0]:cuts2[1]*RULESIZE+remainder[1]] = \
        gMom[cuts[0]*RULESIZE+remainder[0]:cuts[1]*RULESIZE+remainder[1]]
        brother.listSize = len(brother.genomeList)

    return (sister, brother)


def CrossoverDeGabil(genome, **args):
    sister = None
    brother = None
    gMom = args["mom"]
    gDad = args["dad"]
    tamReglas = RULESIZE

    # print len(gMom.genomeList), len(gDad.genomeList)

    cuts = [rand_randint(0, (len(gMom)-1)/ tamReglas) , rand_randint(0, (len(gMom)-1)/tamReglas)]  

    if cuts[0] > cuts[1]:
        Util.listSwapElement(cuts, 0, 1)

    restos = [rand_randint(0, tamReglas-1), rand_randint(0, tamReglas-1)]

    if restos[0] > restos[1]:
        Util.listSwapElement(restos, 0, 1)

    cuts2 = [rand_randint(0, (len(gDad)-1) / tamReglas), rand_randint(0, (len(gDad)-1)/tamReglas)]

    if cuts2[0] > cuts2[1]:
        Util.listSwapElement(cuts2, 0, 1)

    if args["count"] >= 1:
        sister = gMom.clone()
        sister.resetStats()
        sister[cuts[0]*tamReglas+restos[0]:cuts[1]*tamReglas+restos[1]] = \
            gDad[cuts2[0]*tamReglas+restos[0]:cuts2[1]*tamReglas+restos[1]]
        sister.listSize = len(sister.genomeList)
        # print len(sister.genomeList)

    if args["count"] == 2:
        brother = gDad.clone()
        brother.resetStats()
        brother[cuts2[0]*tamReglas+restos[0]:cuts2[1]*tamReglas+restos[1]] = \
            gMom[cuts[0]*tamReglas+restos[0]:cuts[1]*tamReglas+restos[1]]
        brother.listSize = len(brother.genomeList)

    return (sister, brother)


def CrossoverTwoPoint(genome, **args):
    """ The G1DList crossover, Two Point

    .. warning:: You can't use this crossover method for lists with just one element.

    """
    sister = None
    brother = None
    gMom = args["mom"]
    gDad = args["dad"]
       
    if len(gMom) == 1:
        Util.raiseException("The 1D List have one element, can't use the Two Point Crossover method !", TypeError)


    print len(gMom.genomeList), len(gDad.genomeList)

    cuts = [rand_randint(1, len(gMom)-1), rand_randint(1, len(gMom)-1)]

    if cuts[0] > cuts[1]:
        Util.listSwapElement(cuts, 0, 1)

    if args["count"] >= 1:
        sister = gMom.clone()
        sister.resetStats()
        sister[cuts[0]:cuts[1]] = gDad[cuts[0]:cuts[1]]


    if args["count"] == 2:
        brother = gDad.clone()
        brother.resetStats()
        brother[cuts[0]:cuts[1]] = gMom[cuts[0]:cuts[1]]

    return (sister, brother)