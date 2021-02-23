def urlify(string: str, length: int):
    string = [x for x in string]

    for x in range(0, length):
        if x > 1:
            if (string[x-1] and string[x+1] != ' ') and string[x] == ' ':
                string[x] = '%20'

    string = ''.join(string)
    print(string)


if __name__ == '__main__':
    s = 'Mr John Smith  '
    urlify(s, 13)
