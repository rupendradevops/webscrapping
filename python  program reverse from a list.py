
#def reverselist(inputlist):
 #   return inputlist[::-1]
#if  name == "main":
   # mylist = [1, 2, 3, 4, 5]
  #   print("Original list:", mylist)
#    print("Reversed list:", reversedlist)

#myset =frozenset([1,2,3,4,5])
#myfrozenset =frozenset([1,2,3,4,5])
#otherset =frozenset([3,4,5])
#unionset = myfrozenset.union(otherset)
#print(unionset)


#def is_prime(num):
  #  if num < 2:
    #    return False
   # for i in range(2, int(num**0.5) + 1):
  #      if num % i == 0:
 #           return False
#    return True

#def print_primes_in_interval(start, end):
  #       if is_prime(num):

#            print(num)

#if name == " main ":
 #   try:
 #       startinterval = int(input("Enter the start of the interval: "))
    #    endinterval = int(input("Enter the end of the interval: "))
#
         #if startinterval < 0 or endinterval < 0 or startinterval > endinterval:
         print("Invalid input. Start interval should be greater than or equal to 0 and less than or equal to end interval.")
              else:
              print("Prime numbers in the interval:")
            print("primesininterval(startinterval, endinterval")
    except ValueError:

           print("Invalid input. Please enter valid integers for the interval.")

import random
list1=[2,4,5,6,66,55]
print(list1)
random.shuffle(list1)
print(list1)



n = 20
n1, n2 = 1, 2
for i in range(2, n):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3, end='')
    print()

tuple1 = (22, 11, 11, 22, 33, 44, 55)
print(tuple1)
tuple2 = tuple1
tuple2 = 33
print(tuple2)
print(tuple1)

list1 = [22, 33, 44, 22, 1]
print(list1)
list2 = list1
list2.append("hello")
print(list2)
print(list1)

set1 = {22, 33, 22, 1, 44} 
print(set1)
set2 = set1
set2.add(222)

print(set2)
print(set1)





