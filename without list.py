res1 = []
res2 = []
res3 = []
res4 = []
list2 = ['abc', 'xyz', 1, 2, 'pqr', 3,  4, 'a']
for j in list2:
    if(type(j) == int):
        res1.append(j)
    elif(type(j) == str):
        res2.append(j)
    elif(type(j) == float):
        res3.append(j)
    elif(type(j) == bool):
        res4.append(j)

print("Integer list:  " + str(res1))
print("String List: " + str(res2))
print("float List: " + str(res3))
print("bool List: " + str(res4))

######

Employeedetails = []

for i in range(2):
    name = input("Enter Employee name: ")
    number = int(input("Enter Employee Salary: "))
    letter = input("Enter Employee Grade: ")[0]
    Employeedetails.append((name, number, letter))

print("Inputted values:", Employeedetails)
Employeedetails.sort()
print("Employee_details:", Employeedetails)

 

