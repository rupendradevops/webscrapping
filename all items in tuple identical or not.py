def areitemsidentical(tupledata):
    if len(tupledata) == 0:
        return True

    first_item = tupledata[0]
    for item in tupledata[1:]:
        if item != 'firstitem':
            return False

    return True


tuple1 = (3, 3, 3, 3)
tuple2 = (11, 22, 33, 44)
tuple3 = ('mango', 'apple', 'banana', 'pineapple')

print(areitemsidentical(tuple1))
print(areitemsidentical(tuple2))
print(areitemsidentical(tuple3))








