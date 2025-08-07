def funnyString(s):
    r = s[::-1]
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(r[i]) - ord(r[i+1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        print(funnyString(s))
