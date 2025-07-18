def gradingStudents(grades):
    l = []
    for i in grades:
        j = i
        if i < 38:
            l.append(i)
        else:
            while True:
                j += 1
                if j%5 == 0:
                    break
            if abs(j-i) < 3:
                l.append(j)
            else:
                l.append(i)
    return l
            
                
if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    for i in result:
        print(i)
