import random

with open("file1.txt") as file1:
    file_1_data=file1.readlines()
with open("file2.txt") as file2:
    file_2_data=file2.readlines()
number=[int(num) for num in file_1_data if num not in file_2_data]
print(number)

student_list={"david","sara","john","donald"}
student_list_score={
    "student":["david","sara","john","donald"],
    "score":[3,5,10,55]
}
student_score={student:random.randint(1,100) for student in student_list}
student_score_up={student:score for (student,score) in student_score.items() if score>60 }
print(student_score_up)

sentence="Hello, How are you? "
result={word:len(word) for word in sentence.split()}
print(result)

days_of_week={
    "Monday":23,
    "Tuesday":22,
    "Wednesday":12,
    "Thursday":13,
    "Friday":11,
    "Saturday":41,
    "Sunday":3
}
farenheight={day:temp*(9/5)+32 for day,temp in days_of_week.items()}
print(farenheight)

import pandas

imported_dict=pandas.DataFrame(student_list_score)
print(imported_dict)
for (index,row) in imported_dict.iterrows():
     if row.student=="sara":
         print(row.score)