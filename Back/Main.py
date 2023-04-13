from datetime import datetime
from itertools import product

from Date import Date
from SpecialCharacters import SpecialCharacters
from Word import Word


class PasswordGenerator:

    def __init__(self, words, date_value, options):
        self.words = words
        self.date_value = date_value
        self.options = options

    def generate(self):
        result = []
        result.extend(self.words)

        # Add uppercase words
        if self.options['uppercase']:
            result.extend([word.upper() for word in self.words])

        # Add camelcase words
        if self.options['camelcase']:
            result.extend([word.capitalize() for word in self.words])

        # Add leet speak words
        if self.options['leet']:
            result.extend([Word.leet_speak(word) for word in self.words])

        # Add words without accents
        if self.options['remove_accents']:
            result.extend([Word.remove_accents(word) for word in self.words])

        # Add month name
        if self.options['monthname']:
            result.append(self.date_value.strftime('%B').lower())

        # Add year, month and day
        if self.options['add_date']:
            result.append(str(self.date_value.year))
            result.append(str(self.date_value.month))
            result.append(str(self.date_value.day))

        # Add word combinations, max 5
        for idx in range(len(self.words)):
            for idx2 in range(len(self.words)):
                for idx3 in range(len(self.words)):
                    for idx4 in range(len(self.words)):
                        for idx5 in range(len(self.words)):
                            if idx != idx2 and idx != idx3 and idx != idx4 and idx != idx5 and idx2 != idx3 and idx2 != idx4 and idx2 != idx5 and idx3 != idx4 and idx3 != idx5 and idx4 != idx5:
                                result.append(
                                    self.words[idx] + self.words[idx2] + self.words[idx3] + self.words[idx4] + self.words[idx5])

        # Add words with year, month, and day
        for idx in range(len(self.words)):
            result.append(self.words[idx] + str(self.date_value.year))
            result.append(str(self.date_value.year) + self.words[idx])
            result.append(self.words[idx] + str(self.date_value.month))
            result.append(str(self.date_value.month) + self.words[idx])
            result.append(self.words[idx] + str(self.date_value.day))
            result.append(str(self.date_value.day) + self.words[idx])

        # Add special characters
        if self.options['special_characters'] in ['all', 'common']:
            special_chars = SpecialCharacters.get_chars(self.options)
            result = SpecialCharacters.add_chars(
                result, special_chars, self.options['num_special_chars'])

        return result


if __name__ == '__main__':
    words = [input(f'Enter word {i+1}: ') for i in range(
        int(input('Enter the number of words: ')))]

    date_input = input('Enter the date (YYYY-MM-DD): ')
    year, month, day = map(int, date_input.split('-'))
    date = Date()
    date.value = datetime(year=year, month=month, day=day)
    date_value = date.value

    options = {
        'uppercase': input('Do you want to convert your words to uppercase? (y/n) ') == 'y',
        'camelcase': input('Do you want to convert your words to camelcase? (y/n) ') == 'y',
        'leet': input('Do you want to convert your words to leet speak? (y/n) ') == 'y',
        'remove_accents': input('Do you want to remove accents from your words? (y/n) ') == 'y',
        'monthname': input('Do you want to add the month name? (y/n) ') == 'y',
        'add_date': input('Do you want to add the year, month and day? (y/n) ') == 'y',
        'special_characters': input('Do you want to add special characters? (all/common/n) '),
        'num_special_chars': int(input('How many special characters do you want to add? ')),
    }

    generator = PasswordGenerator(words, date_value, options)
    passwords = generator.generate()

    print(passwords)
