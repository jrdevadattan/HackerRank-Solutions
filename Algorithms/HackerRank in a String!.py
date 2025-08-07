def hackerrankInString(s):
    target = "hackerrank"
    i = 0
    for ch in s:
        if i < len(target) and ch == target[i]:
            i += 1
    return "YES" if i == len(target) else "NO"

if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input()
        print(hackerrankInString(s))
