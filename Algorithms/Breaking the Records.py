def breakingRecords(scores):
    l = [0,0]
    s = scores[0]
    b = scores[0]
    for i in scores:
        if i < s:
            l[1] += 1
            s = i
        elif i > b:
            l[0] += 1
            b = i
        else:
            continue
    return l
        
if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    for i in result:
        print(i, end=" ")
