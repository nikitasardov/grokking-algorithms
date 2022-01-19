def count(list):
    if not list:
        c = 0
    else:
        c = 1 + count(list[1:])

    print(c)
    return c


count([1, 2, 3, 4, 5, 6, 7])
# count([])
