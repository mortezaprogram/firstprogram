student_height=[133,524,244,553,224,423,231,131,343,434]
total_student=0
total_student_num=0
for student in student_height:
    total_student+=student
print(total_student)
for student in student_height:
    total_student_num+=1
print(total_student_num)
print(f"The middle of all student is {round(total_student/total_student_num)}")
print(max(student_height))
print(min(student_height))
max_score=0
for score in student_height:
    if score>max_score:
        max_score=score
print(max_score)
