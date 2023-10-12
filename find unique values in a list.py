def uniquevalues(list):
    unique_values = []

    for item in list:
        if item not in unique_values:
            unique_values.append(item)

    return unique_values


my_list = [12,23,45,67,87,65,43,12,23,87]
unique_values = uniquevalues(my_list)
print("Unique values:", unique_values)