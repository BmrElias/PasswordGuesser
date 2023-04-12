from datetime import datetime

from Date import Date
from SpecialCharacters import SpecialCharacters
from Word import Word


class PasswordGuesser:
    def __init__(self, words, options, date):
        self.words = words
        self.options = options
        self.date = date

    def generate(self):
        result = self.words.copy()
        if self.options.get('lowercase'):
            result = [word.lower() for word in result]
        if self.options.get('uppercase'):
            result = [word.upper() for word in result]
            if self.options.get('camelcase'):
                result = [word.capitalize() for word in result]
        if self.options.get('remove_accents'):
            result = [Word.remove_accents(word) for word in result]
        if self.options.get('leet'):
            result = [Word.leet_speak(word) for word in result]
        if self.options.get('use_year'):
            year = self.date.get_year(short=self.options.get('short_year'))
            result += [word + year for word in self.words] + \
                [year + word for word in self.words]
        if self.options.get('use_month'):
            if self.options.get('use_month_name'):
                month_name = self.date.get_month_name(
                    language=self.options.get('language'))
            else:
                month_name = self.date.get_month_number()
            result += [word + month_name for word in self.words] + \
                [month_name + word for word in self.words]
        if self.options.get('use_day'):
            day = self.date.get_day()
            result += [word + day for word in self.words] + \
                [day + word for word in self.words]
        if self.options.get('use_special_chars'):
            chars = SpecialCharacters.get_chars(
                self.options.get('special_chars'))
            num_chars = self.options.get('num_special_chars')
            result = SpecialCharacters.add_chars(result, chars, num_chars)
        max_combinations = self.options.get('max_combinations')
        if max_combinations is not None:
            result = self.get_combinations(result, max_combinations)
        return result

    def get_combinations(self, words, max_combinations):
        result = words.copy()
        for i in range(2, max_combinations + 1):
            for j in range(len(words)):
                for k in range(j + 1, len(words)):
                    if len(words[j]) + len(words[k]) <= i:
                        for l in range(k + 1, len(words)):
                            if len(words[j]) + len(words[k]) + len(words[l]) <= i:
                                for m in range(l + 1, len(words)):
                                    if len(words[j]) + len(words[k]) + len(words[l]) + len(words[m]) <= i:
                                        result.append(
                                            words[j] + words[k] + words[l] + words[m])
        return result


words = []
n_words = int(input('Enter the number of words: '))
for i in range(n_words):
    word = input(f'Enter word {i+1}: ')
    words.append(word)

date_input = input('Enter a date (YYYY-MM-DD): ')
year, month, day = map(int, date_input.split('-'))
date = Date()
date.value = datetime(year=year, month=month, day=day)

options = {
    'lowercase': input('Do you want to convert your word to lowercase? (y/n) ').lower() == 'y',
    'remove_accents': input('Do you want to remove accents? (y/n) ').lower() == 'y',
    'uppercase': input('Do you want to convert your word to uppercase? (y/n) ').lower() == 'y',
    'camelcase': input('Do you want to convert your word to camelcase? (y/n) ').lower() == 'y',
    'leet': input('Do you want to convert your word to leet speak? (y/n) ').lower() == 'y',
    'short_year': input('Do you want to use short year format? (y/n) ').lower() == 'y',
    'language': input('Enter your language for month name (e.g. "en" for English, "fr" for French): '),
    'use_special_chars': input('Do you want to use special characters? (y/n) ').lower() == 'y',
    'special_chars': input('Enter the special characters you want to use (e.g. ".$?!*"): '),
    'num_special_chars': int(input('Enter the number of special characters to add to each password: ')),
    'max_combinations': int(input('Enter the maximum number of elements per combination (max 5): '))
}

guesser = PasswordGuesser(words, options, date)
passwords = guesser.generate()
print('Generated passwords:')
