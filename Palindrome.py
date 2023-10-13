str = input("Enter a string to check whether it is Palindrome or not: ")
strlist=list(str)
strlist.reverse()
rev_str = ''
for i in strlist:

    rev_str = rev_str + i

print(rev_str)
if (str == rev_str):
    print("Given string ",str," is palindrome")

else:
    print("Given string '",str,"' is not palindrome")





