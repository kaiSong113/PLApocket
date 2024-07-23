import matplotlib.pyplot as plt
import numpy as np
import random

x = []
y = []
#input data
for _ in range(20):
    #random data
    vec = np.array([1, random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)])
    x.append(vec)
    y.append(random.choice([1, -1]))
w = np.array([0, 0, 0, 0])
pocket = w
index = 0
safe = 0
#check 200 times to save the best w
for count in range(200):
    #if sign(h(x)) is not same as y:
    if np.sign(np.dot(x[index], w)) != y[index]:
        w = w + y[index] * x[index]
        pocketMis = []
        newMis = []
        # check if the new one is better
        for num in range(len(x)):
            # check the mistake of pocket w
            if np.sign(np.dot(x[num], pocket)) != y[num]:
                pocketMis.append(x[num])
            # check the mistake of new w
            if np.sign(np.dot(x[num], w)) != y[num]:
                newMis.append(x[num])
        #if new w has fewer mistakes, replace pocket by new w
        if len(newMis) < len(pocketMis):
            pocket = w
            MisNum = len(newMis)
        count += 1
        safe = 0 #mistake exist, restart
    #else keep checking
    else:
        index += 1
        safe += 1
        if index == len(x):
            index = 0
        #if there are no mistakes, then quit
        if safe == len(x):
            break
# best w = pocket
wf = pocket
print(f'the best w is {wf} with {MisNum} mistakes.')
