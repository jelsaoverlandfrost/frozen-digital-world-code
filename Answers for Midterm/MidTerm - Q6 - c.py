#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def get_friends(G,node):
    final_list = G[node].keys()
    return final_list

print get_friends({0: {1: 1, 2: 1, 3: 1}, 1: {0: 1, 48: 1, 53: 1}, 2: {0: 1}, 3: {0: 1}, 48: {1: 1}, 53: {1: 1}}, 2)