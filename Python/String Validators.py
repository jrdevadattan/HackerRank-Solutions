if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isnumeric() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
