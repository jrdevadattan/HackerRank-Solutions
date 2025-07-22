def repeatedString(s, n):
    a = len(s)
    r = n // a
    b = n % a
    c = s.count('a') * r
    if b:
        c += s[:b].count('a')
    return c
    
if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
