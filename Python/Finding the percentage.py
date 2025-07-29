if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = student_marks[query_name]
    print(f"{(sum(l)/len(l)):.2f}")
