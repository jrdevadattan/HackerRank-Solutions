def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            count += 1
    return count

if __name__ == '__main__':
    s = input()
    print(marsExploration(s))
