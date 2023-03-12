secret_string=""
norm_string="my_test_for_test"
for char in norm_string:
    secret_string+=str(ord(char)-23)
print(secret_string)
norm_string=""
for i in range(0,len(secret_string)-1,2):
    norm_string+=chr(int(secret_string[i]+secret_string[i+1])+23)

print(norm_string)

