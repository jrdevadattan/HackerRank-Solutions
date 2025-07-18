def plusMinus(ar):
    num = len(ar)
    p = 0
    n = 0
    z = 0
    for i in ar:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    print(f'{p/num}\n{n/num}\n{z/num}')
        
    
    
n = int(input())
l = list(map(int, input().strip().split()))
plusMinus(l)
