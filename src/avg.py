import json

crossover = "0.8"
mutation = "0.01"
parent = "2"
survivor = "1"
population = "60"
generation = "1000"

extension = "cross" + crossover + "_mut" + mutation + "_par" + parent + "_surv" + survivor \
            + "_pop" + population + "_gen" + generation

testFile = open("../tests/"+extension, mode='r')
data = json.load(testFile)

avg,num,cont = 0,0,0

print "Crossover: " + crossover
print "Mutation: " + mutation
print "Parent selection: " + parent
print "Survivor selection: " + survivor
print "Population: " + population
print "Generations: " + generation

for example in data:
    
    if example['correct'] == 0:
    	continue
    cont += 1

    avg += example['correct']
    with open("../data/test/"+example['time']+"_"+extension, mode='r') as f:
        data = json.load(f)
        num += len(data)

print "--------------------------------------"
print "Percentage: %s" %((avg / float(num))*100)
print "Correctly classified: %s" %(avg / float(cont))