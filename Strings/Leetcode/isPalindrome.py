def isPalindrome(s: str):
    if len(s) < 1:
        return False

    s = s.lower()
    s = [x for x in s if x.isalnum()]

    revS = s[::-1]
    if s == revS:
        return True

    return False
    print(s)
    print(revS)


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    # s = 'race a car'
    print(isPalindrome(s))
