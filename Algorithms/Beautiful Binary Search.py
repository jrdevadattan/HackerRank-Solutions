def beautifulBinaryString(b):
    i = 0
    c = 0
    while i < len(b) - 2:
        if b[i:i+3] == '010':
            c += 1
            i += 3
        else:
            i += 1
    return c

if __name__ == '__main__':
    n = int(input())
    b = input()
    print(beautifulBinaryString(b))
