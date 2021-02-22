def insertionSort(arr: list):
    for x in range(1, len(arr)):
        key = arr[x]
        predecessor = x - 1  # index of predecessor
        while predecessor >= 0 and arr[predecessor] > key:
            arr[predecessor + 1] = arr[predecessor]
            predecessor = predecessor - 1
        arr[predecessor + 1] = key

    print(arr)


if __name__ == '__main__':
    a = [17, 25, 31, 13, 2]
    insertionSort(a)
