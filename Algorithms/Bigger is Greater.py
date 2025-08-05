def biggerIsGreater(w):
    l = [ord(i) for i in w]
    i = len(l) - 2
    while i >= 0 and l[i] >= l[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    j = len(l) - 1
    while l[j] <= l[i]:
        j -= 1
    l[i], l[j] = l[j], l[i]
    l[i + 1:] = reversed(l[i + 1:])
    return ''.join(chr(c) for c in l)
    

if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)
        print(result)
