import string
from utils import create_alphabet_letter_encodings


class CeasarEncoder:
    def __init__(self,
                 message: string,
                 k: int,
                 alphabet: list = None):
        if alphabet is None:
            self.alphabet = string.ascii_lowercase
        else:
            self.alphabet = alphabet

        self.letter_to_number, self.number_to_letter = create_alphabet_letter_encodings(self.alphabet)
        self.message = message.lower()
        self.k = k
        self.alphabet_length = len(self.alphabet)

    def encrypt(self):
        print("\nI'm encrypting like the great Emperor for you...")
        chiffre = ""
        for letter in self.message:
            chiffre = chiffre + self.encrypt_letter(letter)
        return chiffre

    def decrypt(self):
        print(f"I'm decrypting like the great Emperor for you...")
        chiffre = ""
        for letter in self.message:
            chiffre = chiffre + self.decrypt_letter(letter)
        return chiffre

    def encrypt_letter(self, letter):
        try:
            vigenere_key = (self.letter_to_number[letter] + self.k) % self.alphabet_length
            res = self.number_to_letter[vigenere_key]
        except KeyError:
            res = letter
        return res

    def decrypt_letter(self, letter):
        try:
            vigenere_key = (self.letter_to_number[letter] - self.k) % self.alphabet_length
            res = self.number_to_letter[vigenere_key]
        except KeyError:
            res = letter
        return res