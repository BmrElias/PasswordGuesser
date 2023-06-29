from datetime import datetime
from itertools import product

from Date import Date
from Options import Options
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
        if self.options.uppercase:
            result.extend([word.upper() for word in self.words])

        # Add camelcase words
        if self.options.camelcase:
            result.extend([word.capitalize() for word in self.words])

        # Add leet speak words
        if self.options.leet:
            result.extend([Word.leet_speak(word) for word in self.words])

        # Add words without accents
        if self.options.remove_accents:
            result.extend([Word.remove_accents(word) for word in self.words])

        # Add month name
        if self.options.monthname:
            result.append(self.date_value.strftime('%B').lower())

        # Add year, month, and day
        if self.options.add_date:
            result.append(str(self.date_value.year))
            result.append(str(self.date_value.month))
            result.append(str(self.date_value.day))

        # Add word combinations, max 5
        for combination in product(self.words, repeat=5):
            if len(set(combination)) == len(combination):
                result.append(''.join(combination))

        # Add words with year, month, and day
        for word in self.words:
            result.append(word + str(self.date_value.year))
            result.append(str(self.date_value.year) + word)
            result.append(word + str(self.date_value.month))
            result.append(str(self.date_value.month) + word)
            result.append(word + str(self.date_value.day))
            result.append(str(self.date_value.day) + word)

        # Add special characters
        if self.options.special_characters in ['all', 'common']:
            special_chars = SpecialCharacters.get_chars(self.options)
            result = SpecialCharacters.add_chars(
                result, special_chars, self.options.num_special_chars)

        return result


if __name__ == '__main__':
    words = [input(f'Enter word {i + 1}: ') for i in range(
        int(input('Enter the number of words: ')))]

    date_input = input('Enter the date (YYYY-MM-DD): ')
    year, month, day = map(int, date_input.split('-'))
    date = Date()
    date.value = datetime(year=year, month=month, day=day)
    date_value = date.value

    options = Options()
    options.uppercase = input(
        'Do you want to convert your words to uppercase? (y/n) ') == 'y'
    options.camelcase = input(
        'Do you want to convert your words to camelcase? (y/n) ') == 'y'
    options.leet = input(
        'Do you want to convert your words to leet speak? (y/n) ') == 'y'
    options.remove_accents = input(
        'Do you want to remove accents from your words? (y/n) ') == 'y'
    options.monthname = input(
        'Do you want to add the month name? (y/n) ') == 'y'
    options.add_date = input(
        'Do you want to add the year, month, and day? (y/n) ') == 'y'
    options.special_characters = input(
        'Do you want to add special characters? (all/common/n) ')
    if options.special_characters in ['all', 'common']:
        options.num_special_chars = int(
            input('How many special characters do you want to add? '))

    generator = PasswordGenerator(words, date_value, options)
    passwords = generator.generate()

    print(passwords)
