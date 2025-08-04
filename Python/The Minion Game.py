def minion_game(string):
    v = 'AEIOU'
    k = 0
    st = 0
    l = len(string)

    for i in range(l):
        if string[i] in v:
            k += l - i
        else:
            st += l - i

    if k > st:
        print("Kevin", k)
    elif st > k:
        print("Stuart", st)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
