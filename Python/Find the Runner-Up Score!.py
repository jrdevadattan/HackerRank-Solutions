if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(set(arr))
    l.sort()
    print(l[-2])
  
