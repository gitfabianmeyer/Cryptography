import string


def num_to_let(alphabet):
    return {i: alphabet[i] for i in range(len(alphabet))}


def reverse_dict(dictionary):
    return {v: k for k, v in dictionary.items()}


def create_alphabet_letter_encodings(alphabet: list):
    number_to_letter = num_to_let(alphabet)
    letter_to_number = reverse_dict(number_to_letter)
    return letter_to_number, number_to_letter