def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = ''
        for c in t:
            if c not in u:
                u += c
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
