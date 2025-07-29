if __name__ == "__main__":
    e = int(input().strip())
    english = set(input().split())
    f = int(input().strip())
    french = input().split()
    print(len(english.symmetric_difference(french)))
    
