my_string=" This is for my test  Hello   "
'''result_stting=print(my_string.lstrip())
result_stting_01=print(my_string.rstrip())
result_stting_02=print(my_string.strip())

result_stting_04=print(my_string.capitalize())
result_stting_05=print(my_string.upper())
result_stting_06=print(my_string.lower())

my_list=["apple","orange","pie"]
my_string_join="".join(my_list)
print(my_string_join)

my_string_replace=my_string.replace("for","four")
print(my_string_replace)
'''
input_string=input("Please input your string")
input_string_upper=input_string.upper()
input_string_split=input_string_upper.split()
for i in input_string_split:
  print(i[0],end="")
print()