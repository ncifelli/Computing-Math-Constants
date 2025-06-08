import random

numTrials = 1000000
count = 0


for i in range(numTrials):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    
    d = x**2 + y**2
    if d <= 1:
        count = count + 1

    


pi = count/numTrials * 4 

print(pi)