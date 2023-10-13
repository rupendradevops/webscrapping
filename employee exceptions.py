class Employee:
    def init(self , name ,id , department , salary , networth):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary
        self.networth = networth
45
    def calculatetaxdeduction(self):
        if self.networth <= 300000:
            tax_rate = 0.0
        elif 300000 < self.networth <= 500000:
            tax_rate = 0.1
        else:
            tax_rate = 0.3
        return self.networth * tax_rate

def displayemployeetable(employees):

    print("{:<15} {:<10} {:<15} {:<10} {:<15} {:<10}".format("NAME","ID","DEPARTMENT","SALARY","NETWORTH","TAXDEDUCTION"))
    for emp in employees:
        taxdeduction = emp.calculate_tax_deduction()
        print("{:<15} {:<10} {:<15} {:<10} {:<15} {:<10}".format(emp.name,emp.id,emp.department,emp.salary,emp.networth,taxdeduction))

def float_input(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print("Enter the Details in Interger Values !:) ")


employees_list = []

numemp = int(input("ENTER THE NUMBER OF EMPLOYEE: "))
for i in range(numemp):
    print(f"\n Enter the Employee details {i + 1}: ")
    name = input("NAME: ")
    id = input("ID: ")
    department = input("DEPARTMENT: ")
    salary = float_input("SALARY: ")
    networth = float_input("NETWORTH: ")

    empobj = Employee(name , id , department , salary , networth)
    employees_list.append(empobj)
print("\n Employee details: ")
displayemployeetable(employees_list)















