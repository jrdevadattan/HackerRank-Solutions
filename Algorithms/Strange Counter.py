def strangeCounter(t):
    m=1
    i=1
    n=0
    while m<=t:
        m=3*i
        if t>n and t<=m:
            return ((m+1)-t)
        i+=i+1
        n=m

if __name__ == '__main__':
    t = int(input().strip())
    result = strangeCounter(t)
    print(result)
