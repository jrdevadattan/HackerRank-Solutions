def countingValleys(steps, path):
    v = 0
    lvl = 0
    for i in range(steps):
        if path[i] == "U":
            lvl += 1
            if lvl == 0:
                v += 1
        else:
            lvl -= 1              
    return v
            
if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
