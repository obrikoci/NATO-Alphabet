import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
print(nato_dict)

def generate():
    word = input("Enter a word: ").upper( )
    try:
        phonetic_code = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters from the alphabet.")
        generate()
    else:
        print(phonetic_code)

generate()