from pandas import pandas

data= pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
phonotic_dict={row.letter:row.code for (index,row) in data.iterrows()}

word=input("Please input your word: ").upper()
output_list=[phonotic_dict[letter] for letter in word]
print(output_list)