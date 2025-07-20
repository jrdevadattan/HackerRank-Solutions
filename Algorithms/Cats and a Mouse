def catAndMouse(x, y, z):
    ca = abs(z-x)
    cb = abs(z-y)
    if ca == cb:
        return "Mouse C"
    elif ca < cb:
        return "Cat A"
    elif ca > cb:
        return "Cat B"

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)
