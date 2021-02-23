def isUnique(string: str) -> bool:
    seen = {}

    for x in range(len(string)):
        if string[x] in seen:
            return False
        else:
            seen[string[x]] = string[x]
    return True


if __name__ == '__main__':
    s = 'string'
    s2 = 'strings'
    print(isUnique(s))
    print(isUnique(s2))
