primeSet = {1,3,5,7,9,11,13}
print("The Items present in the set are : ",primeSet," and Set Size is :",len(primeSet))
fruitSet = {"Banana","Mango","Apple","Grapes","Papaya","Banana"}
print("The Items present in the set are : ",fruitSet," and Set Size is :",len(fruitSet))
mySet = set() # {}---create empty set
mySet = set((1,5,3,6,75,34,3,3,45))
print("The Datatype of mySet :",type(mySet))
print("The items in the Set are : ",mySet," and its Length is :",len(mySet))

numSet = set(range(20,30))
print("The items in the Set are : ",numSet," and its Length is :",len(numSet))
for charIterator in "RUPENDER" :
    mySet.add(charIterator)
    print("The Item present in mySet is :",mySet)

for intIterator in range(1,100):
    mySet.add(intIterator)
print("The items in mySet are :",mySet," and its Length is :",len(mySet))
