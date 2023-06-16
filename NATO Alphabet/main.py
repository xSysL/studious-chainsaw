import pandas

data = pandas.read_csv("NATO Alphabet\\nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato)


def nato1():
    word = input("Enter a word: ").upper()
    output_list = [nato[letter] for letter in word]

    print(output_list)


def nato_loop():
    try:
        nato1()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_loop()


nato_loop()
