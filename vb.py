from itertools import combinations

def findsubsetsofsize(my_set, size):
    subsets = list(combinations(my_set, size))
    return subsets


my_set = {1, 2, 3, 4, 5}
size = 2

subsets = findsubsetsofsize(my_set, size)
print("my_set", size)