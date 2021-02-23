def checkPermutation(string1: str, string2: str):
    string1 = sorted([x for x in string1])
    string2 = sorted([x for x in string2])

    if len(string1) != len(string2):
        return False

    for x in range(len(string1)):
        if string1[x] == string2[x]:
            return True
        else:
            return False
    # print(string1)
    # print(string2)


if __name__ == '__main__':
    s = 'string'
    s2 = 'rintss'
    print(checkPermutation(s, s2))
