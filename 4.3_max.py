def max(l):
    if len(l) >= 1:
        currentMax = l[0]
        maybeMax = max(l[1:])
        if maybeMax != None and maybeMax > currentMax:
            return maybeMax
        else:
            return currentMax
    else:
        return None


print(max([1, -2, -19, -4, -8, 5, -6, -7]))
# print(max([]))
