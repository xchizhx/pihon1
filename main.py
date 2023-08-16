v = [1, 4, 7, 3, 0]


def test(a):
    return a


print(sorted(v, key=test))

# lambda a, b: print(a, b)
