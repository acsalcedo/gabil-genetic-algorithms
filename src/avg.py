import json

extension = "cross0.6_mut0.01_par1_surv1_pop60_gen1000"
testFile = open("../tests/"+extension, mode='r')
data = json.load(testFile)
avg = 0
num = 0

for example in data:

    if example['correct'] == 0:
        continue

    avg += example['correct']
    with open("../data/test/"+example['time']+"_"+extension, mode='r') as f:
        data2 = json.load(f)
        num += len(data2)


print avg / float(num)