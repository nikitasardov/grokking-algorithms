import math


def binarySearch(list, item, low=None, high=None, callNum=None):
    if callNum == None:
        callNum = 1

    if callNum == 1:
        print('input list', list)
        global listLength
        listLength = len(list)
        global maxTries
        maxTries = int(math.log(listLength, 2))
        print('list length', listLength, '| max tries', maxTries)

        print('\nsearching index of "', item, '" in')
        list = selectionSort(list)
        print('sorted list', list)

    if callNum > maxTries:
        print('\nno such element "', item, '"\nor', maxTries,
              'tries are not enough to get index of element\nin', list, '(', listLength, 'elements )')
        return None

    if low == None:
        low = 0
    if high == None:
        high = len(list) - 1

    mid = math.floor((low + high) / 2)
    guess = list[mid]
    if guess == item:
        print('\n[', callNum, ']',
              'low [', low, ']', list[low],
              '| GUESS [', mid, ']', guess,
              '| high [', high, ']', list[high])
        print('[', callNum, '] index of element "', item, '" is', mid)
        return mid

    print('\n[', callNum, ']',
          'low [', low, ']', list[low],
          '| GUESS [', mid, ']', guess,
          '| high [', high, ']', list[high])

    if guess > item:
        high = mid - 1
    else:
        low = mid + 1

    return binarySearch(list, item, low, high, callNum + 1)


def findSmallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def selectionSort(list):
    newList = []
    for i in range(len(list)):
        smallest = findSmallest(list)
        newList.append(list.pop(smallest))
    return newList


my_list = [1, 3, 5, 7, 9, 4, 13, 57, 74, 2, 0, -5, -3, 12, 23, -67, 99]

binarySearch(my_list, 1)  # => 4
# binarySearch(my_list, 8) # => None
