rewards = {'Sun': 4, 'Wind': 0, 'Hail': -8}
transitions = {'Sun': {1: [('Sun', 0.5), ('Wind', 0.5)]},
               'Wind': {1: [('Sun', 0.5), ('Hail', 0.5)]},
               'Hail': {1: [('Wind', 0.5), ('Hail', 0.5)]}}

# rewards = {'PU': 0, 'PF': 0, 'RU': 10, 'RF': 10}
# transitions = {'PU': {'S': [('PU', 1)],
#                       'A': [('PU', 0.5), ('PF', 0.5)]},
#                'PF': {'S': [('PU', 0.5), ('RF', 0.5)],
#                       'A': [('PF', 1)]},
#                'RU': {'S': [('PU', 0.5), ('RU', 0.5)],
#                       'A': [('PU', 0.5), ('PF', 0.5)]},
#                'RF': {'S': [('RU', 0.5), ('RF', 0.5)],
#                       'A': [('PF', 1)]}}

d1, d2 = dict(rewards), dict(rewards)
discountFactor = 0.9
tolerance = 1e-3

count = 0
while True:
    for i in transitions:
        m = -float('inf')
        for j in transitions[i]:
            m = max(m, sum([k[1] * d2[k[0]] for k in transitions[i][j]]))
        d1[i] = rewards[i] + discountFactor * m
    delta = max([abs(d1[k] - d2[k]) for k in d1])
    if delta < tolerance: break
    d2 = dict(d1)
    count += 1
print(d1, count)
