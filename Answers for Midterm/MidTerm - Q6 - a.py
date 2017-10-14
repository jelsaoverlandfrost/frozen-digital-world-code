#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.


def get_nodes(fid):
    list_nodes = fid.readlines()
    final_list = []
    for i in list_nodes:
        string_list = i.split()
        final_list.append((int(string_list[0]), int(string_list[1])))
    return final_list