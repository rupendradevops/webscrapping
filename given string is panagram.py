mystr="priyanka"
sri=mystr.replace(" ","")
print(sri)
mylist=list(set(sri))
print(mylist)
mylist.sort()
print(mylist)
alpha=list('abcdefghijklmnopqrstuvwxyz')
if mylist==alpha:
    print("this is a panagram")
else:
    print("this is not a panagram")


  ########
def updatefirstset(set1, set2):
    itemtoadd = set1.difference(set2)

    set1 |= itemtoadd

    return set1


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

updatedset1 = updatefirstset(set1, set2)
print("Updated set1:", updatedset1)

########

from itertools import combinations

def findsubsetsofsize(my_set, size):
    subsets = list(combinations(my_set, size))
    return subsets


my_set = {1, 2, 3, 4, 5}
size = 2

subsets = findsubsetsofsize(my_set, size)
print("my_set", size)

#####
def finduniqueelements(set1, set2):
    uniqueset1 = set1.difference(set2)

    uniqueset2 = set2.difference(set1)
    uniqueelements = uniqueset1.union(uniqueset2)

    return uniqueelements

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

uniqueelements = finduniqueelements(set1, set2)
print("Unique elements:", uniqueelements)

####

def settostring(someset):

    sortedlist = sorted(list(someset))
    stringlist = [str(element) for element in sortedlist]
    resultstring = ', '.join(stringlist)

    return resultstring
set = {1, 2, 3, 4, 5}
result = settostring(set)
print(result)
