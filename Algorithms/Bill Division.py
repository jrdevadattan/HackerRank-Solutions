def bonAppetit(bill, k, b):
    l = bill.copy()
    l[k] = 0
    fair = sum(l)/2
    if b == fair:
        return "Bon Appetit"
    else:
        return int(b - fair)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    r = bonAppetit(bill, k, b)
    print(r)
