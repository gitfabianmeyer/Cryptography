import math

class Skytala:
    def __init__(self, message, k, padding_token = "_"):
        self.message= message
        self.rows = k
        self.columns = math.ceil(len(message)/k)
        self.skytala_length = self.columns * self.rows
        self.padding_token = padding_token.upper()
        self.padded_message = message

    def pad(self):
        padder = ""
        if len(self.message) % self.columns != 0:
            padder = self.get_padder(length= self.skytala_length - len(self.message))

        pad_msg = self.message + padder
        self.padded_message = pad_msg[:self.skytala_length]


    def get_padder(self, length):
        pad = ""
        while len(pad) < length:
            pad = pad + self.padding_token
        return pad

    def encrypt(self):
        print("\nI'm writing on this edgy roll...")
        return self.do_the_magic()

    def build_sk_matrix(self):
        res = []
        for row in range(self.rows):
            res.append([self.padded_message[column + row*self.columns] for column in range(self.columns)])

        return res

    def do_the_magic(self):
        self.pad()
        mat = self.build_sk_matrix()
        res = ""
        for column in range(self.columns):
            for row in range(self.rows):
                res = res + mat[row][column]
        return res