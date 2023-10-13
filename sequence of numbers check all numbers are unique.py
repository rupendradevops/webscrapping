def test_distinct(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False;
print(test_distinct([1,4,7,9]))
