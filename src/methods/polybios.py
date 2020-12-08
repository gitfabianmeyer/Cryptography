import string


class PolybiosEncoder:
    def __init__(self, message, matrix_size = 5):
        self.lookup_table = self.create_encrypter(matrix_size)
        self.message = message

    def create_encrypter(self, matrix_size):
        return [[string.ascii_lowercase[j + (i * matrix_size)] for j in range(matrix_size)] for i in range(matrix_size)]

    def lookup(self, number:string):
        assert len(number) == 2
        assert number.isnumeric()
        return self.lookup_table[int(number[0])-1][int(number[1])-1]

    def decrypt(self):
        print("\nThe old Greek Polybios is working hard for you...")
        assert len(self.message) % 2 == 0

        text = ""
        for i in range(0, len(self.message), 2):
            text = text + self.lookup(self.message[i:i+2])

        return text

