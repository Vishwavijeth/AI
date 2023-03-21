# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:34:56 2023

@author: Arjuna
"""
import numpy as np
states = ['H','L']
initial_prob = {'H' : 0.5,'L' : 0.5}
transitions_prob = {'H':{'H':0.5,'L':0.5},'L' : {'H':0.4,'L':0.6}}
emission_prob = {'H' : {'A':0.2,'G':0.3,'C':0.3,'T':0.2},
                 'L' : {'A':0.3,'G':0.2,'C':0.2,'T':0.3}}

sequence="GGCA"

probability_table = np.zeros([len(states),len(sequence)])


for i in range(len(sequence)) : 
    element = sequence[i]
    if(i==0):
        for j in range(len(states)) :
            probability_table[j][i] = initial_prob[states[j]] * emission_prob[states[j]][element]
    else : 
        for k in range(len(states)) : 
            p1=0
            for j in range(len(states)) : 
                p = probability_table[j][i-1]
                q = transitions_prob[states[j]][states[k]] * emission_prob[states[k]][element]
                p1+=p*q
            probability_table[k][i] = p1

print("Probability table : ",probability_table,sep='\n')

expected =0 
for i in range(len(states)) : 
    expected += probability_table[i][-1]
print("Required probability for the given sequence  : ",expected)
