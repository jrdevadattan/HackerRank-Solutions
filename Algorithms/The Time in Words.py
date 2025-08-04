def timeInWords(h, m):
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen",
         "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three",
         "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    if m == 0:
        return f"{n[h]} o' clock"
    elif m == 15:
        return f"quarter past {n[h]}"
    elif m == 30:
        return f"half past {n[h]}"
    elif m == 45:
        return f"quarter to {n[h+1]}"
    elif m < 30:
        return f"{n[m]} minute{'s' if m != 1 else ''} past {n[h]}"
    else:
        return f"{n[60 - m]} minute{'s' if 60 - m != 1 else ''} to {n[h + 1]}"

if __name__ == '__main__':
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
