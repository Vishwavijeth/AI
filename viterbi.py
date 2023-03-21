# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:34:56 2023

@author: Arjuna
"""
import numpy as np
states = ['H','L']
initial_prob = {'H' : -1,'L' : -1}
transitions_prob = {'H':{'H':-1,'L':-1},'L' : {'H':-1.322,'L':-0.737}}
emission_prob = {'H' : {'A':-2.322,'G':-1.737,'C':-1.737,'T':-2.322},
                 'L' : {'A':-1.737,'G':-2.322,'C':-2.322,'T':-1.737}}


sequence = 'GGCACTGAA'

#Stroring the values for each recursive call (memoization)
probability_table = np.zeros([len(sequence),len(states)])

def viterbi(state,index,position) : 
    #base condition
    if(index==0) : 
        #print(initial_prob[state] + emission_prob[state][sequence[index]])
        probability_table[index][states.index(state)] = (initial_prob[state] + emission_prob[state][sequence[index]])
        return initial_prob[state] + emission_prob[state][sequence[index]]
    else : 
        #If this has already been calculated and stored then no need to calculate again
        x=probability_table[index][states.index(state)]
        if(x!=0):
            return x
        #else call the function recursively for decremented value of index
        emission = emission_prob[state][sequence[index]] 
        values = []
        for j in states : 
            p = transitions_prob[j][state] + viterbi(j,index-1,position-1)
            values.append(p)
        #print(emission + max(values))
        probability_table[index][states.index(state)] = emission + max(values)
        return emission + max(values)

#calling the function for each ending state along with the index of last element
for i in states : 
    viterbi(i,len(sequence)-1,len(sequence))

path=[]
probability_table = probability_table.tolist()
#finding the path (max)
for i in probability_table : 
    path.append(states[i.index(max(i))])    

print("probability table : ")
for i in probability_table : 
    print(i)

print("Path : ",path)