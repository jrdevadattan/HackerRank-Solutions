def camelcase(s):
    c = 1
    for ch in s:
        if 'A' <= ch <= 'Z':
            c += 1
    return c

if __name__ == '__main__':
    s = input()
    result = camelcase(s)
    print(result)
