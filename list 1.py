myList = [1,2,23,45,545,34,34,23]
fruitList=["banana","Mango","Jackfruit","Apple","Orange","Mango"]
mixedList =["Banana",34,34.67,"Mangoe","Apple",55]
nestedList = [[12,4,45,56,23,45],23,"Mango","Apple",45,["Banana","Papaya","Orange","Apple"]]
print("This is integer List \n:",myList)
print("the Value at index :7 \n",myList[7])
print("This is String List \n:",fruitList)
print("the Value at index :1 \n",fruitList[1])
print("the Value at index :5 \n",fruitList[-1])
print("This is Mixed List \n:",mixedList)
print("the Value at index :1 \n",mixedList[1])
print("The list between given range :, \n",mixedList[1:5])
print("The myList and fruitList are added :\n",(myList+fruitList)*3)
print("Repeat list for 6 :\n",myList*6)
print("Find the value mangoe is there in mixedList :",("Mangoe" not in mixedList))
mixedList.append("Rajkumar")
print("This is Mixed List \n:",mixedList)
del mixedList[4]
print("List after deleting last item :\n",mixedList)


