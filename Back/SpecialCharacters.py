import random
import string


class SpecialCharacters:
    @staticmethod
    def get_chars(chars):
        if chars == 'all':
            return string.punctuation
        else:
            return chars

    @staticmethod
    def add_chars(passwords, chars, num_chars):
        if not chars:
            return passwords
        result = []
        for password in passwords:
            for i in range(num_chars):
                pos = random.randint(0, len(password))
                result.append(password[:pos] +
                              random.choice(chars) + password[pos:])
        return result
