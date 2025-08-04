def kaprekarNumbers(p, q):
    c = 0
    for i in range(p,q+1):
        d = len(str(i))
        a = str(i**2)
        if sum([int(a[-d:]), int(a[:-d]) if a[:-d] != '' else 0]) == i:
            c += 1
            print(i, end = ' ')
    if c == 0:
        print("INVALID RANGE")
        

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
