import pandas

data = pandas.read_csv("NATO Alphabet\\nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato)

word = input("Enter a word: ").upper()
output_list = [nato[letter] for letter in word]

print(output_list)
