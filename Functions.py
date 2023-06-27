#Single responsbility principle
#Function definition
#Function calling
#Arguments
#Return statement

#Simulate the coin toss experiment with p=0.5,1000 trials

import random

num_trials=1000
simulation_list=[]
for i in range(num_trials):
    simulation_list.append(
        random.choice(['Head','Tail'])
        )
print("Head's count: ",simulation_list.count('Head'))
print("Tail's count: ",simulation_list.count('Tail'))
    
### Time and Space Complexity: O(n) ####

import random

p=0.3
num_trials=1000
simulation_list=[]
for i in range(num_trials):
    simulation_list.append(
        random.choice(['Head']*int(p*10) +
                      ['Tail']*int((1-p)*10))
        )
print("Head's count: ",simulation_list.count('Head'))
print("Tail's count: ",simulation_list.count('Tail'))
