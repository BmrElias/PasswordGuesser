import random
import string


class SpecialCharacters:
    @classmethod
    def get_chars(cls, options):
        if options['special_characters'] == 'all':
            return string.punctuation
        elif options['special_characters'] == 'common':
            return '.$?!*'
        else:
            return ''

    @classmethod
    def add_chars(cls, passwords, special_chars, num_special_chars):
        if special_chars == '':
            return passwords
        result = []
        for password in passwords:
            num_chars = random.randint(0, num_special_chars)
            for i in range(num_chars):
                pos = random.randint(0, len(password))
                result.append(password[:pos] +
                              random.choice(special_chars) + password[pos:])
        return result
