def countApplesAndOranges(s, t, a, b, apples, oranges):
    l = [0,0]
    al = []
    for i in apples:
        al.append(i+a)
    ol = []
    for j in oranges:
        ol.append(j+b)
    for x in al:
        if s <= x <= t:
            l[0] += 1
    for y in ol:
        if s <= y <= t:
            l[1] += 1
    return l

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    r = countApplesAndOranges(s, t, a, b, apples, oranges)
    for i in r:
        print(i)
