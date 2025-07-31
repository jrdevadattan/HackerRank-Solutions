def acmTeam(topic):
    n = len(topic)
    num = len(topic[0])
    d = {}
    for i in range(n):
        for j in range(i + 1, n):
            c = 0
            for k in range(num):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    c += 1
            d[c] = d.get(c, 0) + 1
    m = max(d)
    return [m, d[m]]
                
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    for i in result:
        print(i)
