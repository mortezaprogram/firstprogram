import re
'''
if re.search("test","This is a test"):
    print("There is test in sentence")
my_text=re.findall("test.","This is for test testscentence")

my_text1= "This is for test testscentence between testtime"


#for i in my_text:
#   print(i)

for i in re.finditer("test.",my_text1):
    locate_word=i.span()
    print(locate_word)
    print(my_text1[locate_word[0]:locate_word[1]])


animal_str="Pat rat cat mat fat"
animal_all=re.findall("[prcmf]at",animal_str)
for i in animal_all:
    print(i)
    print()
animal_all_range=re.findall("[i-zI-Z]at",animal_str)
for i in animal_all_range:
    print(i)
    print()
some_animal=re.findall("[^r]at",animal_str)
for i in some_animal:
    print(i)

owl_list="pat rat cat mat fat"
regex=re.compile("[pr]at")
replace_owl=regex.sub("owl",owl_list)
print(replace_owl)
rand_str="Here is \\stuff"
print("Find \\stuff: ",re.search("\\stuff",rand_str))
print("Find \\stuff: ",re.search("\\\\stuff",rand_str))
print("Find \\stuff: ",re.search(r"\\stuff",rand_str))


rand_str="F.B.I. I.R.S. CIA"
print("Matches: ",len(re.findall(".\..\..",rand_str)))
new_str="""This is a long string 
that is goes on 
for many lines"""
regex=re.compile("\n")
new_str=regex.sub("",new_str)
print(new_str)
rand_str="12345asd"
print("Matches: ",len(re.findall("\D",rand_str)))
if re.search("\d{5}",rand_str):
    print("It is a zip code. ")
rand_str_01="123 12345 123456 1234567 123456789"
print("Matches: ",len(re.findall("\d{5,7}",rand_str_01)))
phone_number="412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}",phone_number):
    print("It is a phone number. ")
if re.search("\w{2,20}","my_name"):
    print("It is a valid name. ")
if re.search("\w{2,20}\s\w{2,20}","david Putin"):
    print("It is a valid full_name. ")
print("Matches: ",len(re.findall("a+","a ape is in apex")))
emailList = "db@aol.com db5@aol.com m@.com @apple.com db@.com db1@aol.com db6@aol.com"
print("Email Matches :", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",emailList)))


rand_string="cat cats"
regex=re.compile("[cat]+s")
rand_string_01=re.findall(regex,rand_string)
print(rand_string_01)
print("Matches: ",len(rand_string_01))
for i in rand_string_01:
    print(i)
    print()
string_test="doctor doctors doctor's"
regex=re.compile("[doctor]+['s]*")
string_test_01=re.findall(regex,string_test)
print("matches: ",string_test_01)
regex01=re.compile("[doctor]+['s]{2,2}")
string_test_02=re.findall(regex01,string_test)
print("Matches: ",len(string_test_02))
for i in string_test_02:
    print(i)

long_str = "Just some words \n and some more\r \n and more "


print("Matches :", len(re.findall(r"[\w\s]+[\r]?\n", long_str)))
matches = re.findall("[\w\s]+[\r]?\n", long_str)
for i in matches:
   print(i)
  
rand_str = "<name>Life On Mars</name><name>Freaks and Geeks</name>"

regex = re.compile(r"<name>.*</name>")
rand_str_02=re.findall(regex,rand_str)
print("Matches: ",len(rand_str_02))
print( (rand_str_02))
for i in rand_str_02:
    print(i)
    print()
    print()
regex01=re.compile(r"<name>.*?</name>")
rand_str_03=re.findall(regex01,rand_str)
print(rand_str_03)
print("Matches: ",len(rand_str_03))
for i in rand_str_03:
    print(i)
print()

rand_str="ape in the apex"
regex=re.compile(r"\bape\b")
rand_str01=re.findall(regex,rand_str)
regex01=re.compile(r"\bape\b")
rand_str02=regex01.sub("ttt",rand_str)
print(rand_str01)
print(rand_str02)



rand_str="match everything up to @"
regex=re.compile(r"^.*[^@]")
rand_str_01=regex.sub("test",rand_str)
print(rand_str_01)
rand_str01="@get this string"
regex=re.compile(r"[^@\s].*$")
rand_str02=regex.sub("end",rand_str01)
print(rand_str02)

rand_str = "Ape is big \n Turtle is slow \n Cheetah is fast"
regex=re.compile(r"(?m)^.*?\s")
rand_str01=regex.sub("test",rand_str)
print(rand_str01)


rand_str="433-432-6577"
regex=re.compile(r"433-(.*)")
rand_str_01=regex.sub("001",rand_str)
print(rand_str_01)

rand_str="412-555-1212 412-555-1213 412-555-1214"
regex=re.compile(r"412-(.{8})")
rand_str01=regex.sub("test",rand_str)
print(rand_str01)

rand_str="412-555-1212"
regex=re.compile(r"412-(.*)-(.*)")
rand_str01=re.findall(regex,rand_str)
print(rand_str01[0][0])
print(rand_str01[0][1])

rand_str="The cat cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = regex.sub("test", rand_str)
print(matches)


rand_str = "<a href='#'><b>The Link</b></a>"
regex = re.compile(r"<b>(.*?)</b>")
rand_str = re.sub(regex,r"\1", rand_str)
print(rand_str)


rand_str="412-435-8976"
regex=re.compile(r"([\d]{3})-([\d]{3})-([\d]{4})")
rand_str01=re.sub(regex,r"(\1)[\2](\3)",rand_str)
print(rand_str01)

rand_str = "https://www.youtube.com http://www.google.com"
regex=re.compile(r"(https?://([\w.]+))")
rand_str01=re.sub(regex,r"<a href='\1'>\2<\a>\n",rand_str)
print(rand_str01)



rand_str = "One two three four"
regex=re.compile(r"\w.+(?=\b)")
rand_str01=re.findall(regex,rand_str)
for i in rand_str01:
    print(i)
print(len(rand_str01))

rand_str = "1. Bread 2. Apples 3. Lettuce"
regex=re.compile(r"(?<=\d.\s)\w+")
rand_str01=re.findall(regex,rand_str)
for i in rand_str01:
    print(i)

rand_str = "<h1>I'm Important</h1> <h1>So am I</h1>"
regex=re.compile(r"(?<=<h1>).+?(?=</h1>)")
rand_str01=re.findall(regex,rand_str)
for i in rand_str01:
    print(i)

rand_str = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, rand_str)
print(len(matches))
matches = [int(i) for i in matches]
from functools import reduce
print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))


rand_str = "1. Dog 2. Cat 3. Turtle"
regex = re.compile(r"\d\.\s(Dog|Cat)")
rand_str01=re.findall(regex,rand_str)
print(rand_str01)


rand_str = "12345 12345-1234 1234 12346-333"
regex=re.compile(r"\d{5}-\d{4}|\d{5}")
rand_str01=re.findall(regex,rand_str)
for i in rand_str01:
    print(i)

bd=input("Pleae input your birthday: ")
bd_regex=re.search(r"\d{1,2}-\d{1,2}-\d{4}",bd)
print("You were born on: ",bd_regex.group())
print("You were born on day: ",bd_regex.group(1))
print("You were born on month: ",bd_regex.group(2))
print("You were born on year: ",bd_regex.group(3))


match=re.search(r"\d{2}","His weight id 55 LB" )
print(match)
print("Match: ",match.group())
print("Span :", match.span())
print("Match :", match.start())
print("Match :", match.end())

rand_str = "December 21 1974"
regex = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"
matches = re.search(regex, rand_str)
print("Month :", matches.group('month'))
print("Day :", matches.group('day'))
print("Year :", matches.group('year'))

rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL brrrb@kkgrt.com"
regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
matches = re.findall(regex, rand_str)
print(len(matches))
for i in matches:
 print(i)
 
 '''
rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
regex = re.compile(r"((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\) )?(\d{3})(-| )?(\d{4}|\d{4}))")
matches = re.findall(regex, rand_str)
print(len(matches))
for i in matches:
 print(i[0].lstrip())





























