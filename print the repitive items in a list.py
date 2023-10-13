def printrepetitiveitems(list):
    seen = set()
    repeated = set()

    for item in list:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)

    print("Repetitive items:")
    for item in repeated:
        print(item)


my_list = [23,23,45,6,78,98,67,43,6,98,78,95]

print(my_list)