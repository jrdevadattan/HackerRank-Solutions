def palindromeIndex(s):
    def is_palin(a, b):
        return s[a:b+1] == s[a:b+1][::-1]
    
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if is_palin(i+1, j):
                return i
            elif is_palin(i, j-1):
                return j
            else:
                return -1
        i += 1
        j -= 1
    return -1

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        print(palindromeIndex(s))
