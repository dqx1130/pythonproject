students = []
while True:
    line = input().strip()
    if line == "#":
        break
    data = line.split()
    student_id = data[0]
    name = data[1]
    scores = list(map(int, data[2:]))
    total_score = sum(scores)
    students.append((student_id, name, total_score))
# 按总分升序排序
students.sort(key=lambda x: x[2])
# 输出结果
for student in students:
    print(f"{student[0]}, {student[1]}, {student[2]}")
