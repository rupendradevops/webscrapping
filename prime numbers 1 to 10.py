start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

start =  int(input("Enter the start of range: "))
end   =  int(input("Enter the end of range: "))

for num in range(start, end + 1):
   if num > 1:

         if (num %i) == 0:
               break
         else:
           print(num)

########

num = int(input("enter a number:"))
def sum(n):
    if n <=1:
        return n
    else:
        return n + sum(n-1)
print("the sum is:",sum(num))
