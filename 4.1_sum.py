def sum(list):
    if not list:
        s = 0
    else:
        s = list.pop() + sum(list)

    # print(s)
    return s


print(sum([1, 2, 3, 4, 5, 6, 7]))
# sum([])
