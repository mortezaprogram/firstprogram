import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
   my_file.write("\n\nthis is a test 1\nPut the words in a list using the space as test 2\nthere is a test 3\n")
with open("mydata.txt", encoding="utf-8") as my_file:
   print(my_file.closed)
   print(my_file.mode)
   print(my_file.name)
#os.rename("mydata.txt","mydata.txt2")
#os.mkdir("mydir")
#os.chdir("pythonProject")
print("current directory is: ",os.getcwd())
with open("mydata.txt", encoding="utf-8") as my_file:
   lineNum=1
   while True:
      line=my_file.readline()
      if not line:
         break
      print("line",lineNum,":",line,end="")
      word_list = line.split()
      print("Number of the words", len(word_list))
      char_count=0
      for word in word_list:
         for chaar in word:
            char_count+=1
      print("Number of the char",char_count)
      #average=char_count/len(word_list)
      if (len(word_list))==0:
         print("Average of the char:  0" )
      else:
         print("Average of the char:{:.2}".format(char_count/len(word_list)))


      lineNum += 1
