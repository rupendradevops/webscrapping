myList = list()
emptyList = [1,3,5,"ST1","ST2","10.43",9.5,10]
print("The myList structure and its length : ",myList,"::",len(myList))
print("The emptyList structure and its length : ",emptyList,"::",len(emptyList))

intList = [23,33,45,23,45,23]
print("The items in the intList is : ",intList)
add5List = intList + [5]
mult5List = intList * 5
print("The list items between position 5 to 50 :", mult5List[32:51])
del mult5List[0:44]
print("The items in the intList is : ",add5List)
print("The items in the intList is : ",mult5List)
fruitList=["Banana","Apple","Mango","Banana","Lemon","apple"]
print("The items in the fruitList is : ",fruitList)
mixedList = intList + fruitList
print("The items int he mixedList are : ",mixedList)
print("The list item access using for loop :")

for intIterator in intList :
    intIterator = intIterator * 5
    print("The items in the intList is :", intList)
    print("The intList item is  : ",intIterator)
print("The size of intList is : ",len(intList))

mixedList.append("10.45")
mixedList.append("sunil")
mixedList.append([1,3,5,'a','e','i','o','u'])
print("The length of the mixedList  is : ",len(mixedList))
print("The Item Sunil is present in mixed List : ","sunil" in mixedList)
mixedList.insert(17,"Chaitanya")
print("The Item at 10 position in mixedList is : ",mixedList[9])
print("Insert PineApple at 10 position in mixedList :")
mixedList.insert(9,"PineApple")
print("The Item at 10 position in mixedList is : ",mixedList[9])
for mixIterator in mixedList :
    print("The Item present in the Mixed List is : ",mixIterator,"\n")
    #del intList

intList.clear()
print("The size of intList  after deletion of item is : ",len(intList))
intList.append(10)
intList.append(34)
intList.append(25)
intList.append(55)
intList.pop()
intList.reverse()

stName = "David"
charList = list(stName)
print("The items in the charList :",charList)
paladrmList = ['M','A','L','A','Y','A','L','A','M']
print("The Palandrome members in the List is :",paladrmList)
paladrmList.reverse()
print("The item 'A' present in the List for  :",paladrmList.count('A'))
print("The Palandrome members in the List after reversing is :",paladrmList)
print("The items in the intList is :", intList)
print("The sum of  items in the intList is :",sum(intList))
#print("The max value item in the List is : ",max(intList))
print("The size of the fruitList is :",len(fruitList))
print("The items of the fruitList is :",fruitList)
print("The min value item in the List is : ",min(fruitList))


