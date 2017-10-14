#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def create_graph(nodes):
    friends_dictionary = {}
    for i in range(len(nodes)):
        for j in (0, 1):
            if nodes[i][j] in friends_dictionary:
                continue
            else:
                number_store = nodes[i][j]
                personal_dict = {}
                for k in nodes:
                    for l in (0, 1):
                        if k[l] == number_store:
                            personal_dict[k[l - 1]] = 1
                friends_dictionary[number_store] = personal_dict
    return friends_dictionary


print create_graph([(0, 1), (0, 2), (0, 3), (1, 48), (1, 53)])
