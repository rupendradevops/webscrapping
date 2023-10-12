def copyelements(originaltuple, indices):
    newtuple = ()
    for index in indices:
        if 0 <= index < len(originaltuple):
            newtuple += (originaltuple[index],)
    return newtuple


tuple1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
indicestocopy = [1, 3, 5]

newtuple = copyelements(tuple1, indicestocopy)

print(newtuple)
