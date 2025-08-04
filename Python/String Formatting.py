def print_formatted(n):
    w = len(bin(n)) - 2
    for i in range(1, n + 1):
        d = str(i).rjust(w)
        o = oct(i)[2:].rjust(w)
        h = hex(i)[2:].upper().rjust(w)
        b = bin(i)[2:].rjust(w)
        print(d, o, h, b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
