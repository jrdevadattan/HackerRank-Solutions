def timeConversion(s):
    a=s[0:2]
    if s[8:10]=='PM' and int(a)!=12:
        a=str(int(a)+12)
    if s[8:10]=='AM' and int(a)==12:
        a='00'
    a = a + s[2:8]
    return a


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
