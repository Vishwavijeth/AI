
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:41:13 2023

@author: 20pt04
"""

states=['Sun','Wind','Hail']
initial_reward={'Sun':4,'Wind':0,'Hail':-8}
actions=['a']
transition_prob={('Sun','a'):[[0.5,'Wind'],[0.5,'Sun']],('Wind','a'):[[0.5,'Hail'],[0.5,'Sun']],('Hail','a'):[[0.5,'Hail'],[0.5,'Wind']]}


prev_reward=initial_reward
current_reward={}

for k in range(120):    
    current_reward={}    
    for i in states:
        val=[] 
        for j in actions: 
            t=transition_prob[(i,j)]
            r=0
            for x in t:
               r+=x[0]*prev_reward[x[1]]
            val.append(r)
        current_reward[i]=initial_reward[i] + 0.9*max(val)
    prev_reward=current_reward
print(prev_reward)