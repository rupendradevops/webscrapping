def swaptuples(tuple1, tuple2):
    return tuple2, tuple1


tuple1 = (11, 12, 13)

tuple2 = (14, 15, 16)

tuple1, tuple2 = swaptuples(tuple1, tuple2)

print("Tuple 1:", tuple1)

print("Tuple 2:", tuple2)
