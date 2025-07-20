def designerPdfViewer(h, word):
    l = len(word)
    c = 0
    b = sorted(list(word))
    for i in b:
        a = ord(i) - 97
        if h[a] > c:
            c = h[a]    
    return c * l

if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    print(result)
