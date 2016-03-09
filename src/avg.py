import json
cross = "0.9"
mut = "0.01"
extension = "cross"+cross+"_mut"+mut+"_par1_surv0_pop20_gen1000"
testFile = open("../tests/"+extension, mode='r')
data = json.load(testFile)
avg = 0
num = 0
cont = 0
print "cross: " + cross
print "mut: " + mut
for example in data:
    if example['correct'] == 0:
	continue
    cont += 1
    avg += example['correct']
    with open("../data/test/"+example['time']+"_"+extension, mode='r') as f:
        data2 = json.load(f)
        num += len(data2)
	

print avg / float(num)
print avg / float(cont)
