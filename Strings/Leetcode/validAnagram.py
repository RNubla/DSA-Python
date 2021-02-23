def isAnagram(s: str, t: str):

    s = sorted([x for x in s])
    t = sorted([x for x in t])

    if s == t:
        return True

    return False


if __name__ == '__main__':
    s = 'anagram'
    t = 'nagaram'

    s1 = 'rat'
    t2 = 'car'

    print(isAnagram(s, t))
    print(isAnagram(s1, t2))
