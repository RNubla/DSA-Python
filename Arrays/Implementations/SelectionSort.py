def selectionSort(arr: list):
    for x in range(len(arr)):
        minElement = x
        for y in range(x + 1, len(arr)):
            if arr[minElement] > arr[y]:
                minElement = y
        arr[x], arr[minElement] = arr[minElement], arr[x]

    return arr
    # print(arr)


if __name__ == '__main__':
    a = [64, 25, 12, 22, 11]
    # a = [5, 2, 6, 7, 2, 1, 0, 3]
    # selectionSort(a)
    sortedArr = selectionSort(a)
    for x in range(len(sortedArr)):
        print(f'{sortedArr[x]}')
