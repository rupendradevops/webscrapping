def findcommonitems(list1, list2):
    commonitems = set(list1) & set(list2)
    return list(commonitems)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

commonitems = findcommonitems(list1, list2)
print("Common items:", commonitems)