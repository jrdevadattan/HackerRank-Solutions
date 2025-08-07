def fairRations(B):
    c = 0
    for i in range(len(B)-1):
        if B[i] % 2 != 0:
            B[i+1] += 1
            c += 2
    return "NO" if B[-1] % 2 != 0 else c
        
if __name__ == '__main__':
    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    print(result)
