import string
from utils import create_alphabet_letter_encodings

class VigenereEncoder:
    def __init__(self,
                 message: string,
                 key: string,
                 alphabet: list = None):
        if alphabet is None:
            self.alphabet = string.ascii_lowercase
        else:
            self.alphabet = alphabet

        self.letter_to_number, self.number_to_letter = create_alphabet_letter_encodings(self.alphabet)
        self.message = message.lower()
        self.key = key.lower()
        self.period_length = len(key)
        self.dict_length = len(self.alphabet)

    def encrypt(self):
        print("\nI'm encrypting like Monsieur Vigenere for you...")
        chiffre = ""
        for i, letter in enumerate(self.message):
            chiffre = chiffre + self.encrypt_letter(letter, i)
        return chiffre

    def encrypt_letter(self, letter, i):
        vigenere_key = (self.letter_to_number[letter] +
                        self.letter_to_number[self.key[i % self.period_length]]) \
                       % self.dict_length
        return self.number_to_letter[vigenere_key]