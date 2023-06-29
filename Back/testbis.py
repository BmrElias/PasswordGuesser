from datetime import datetime


class Word:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Date:
    def __init__(self, date_value):
        self.date_value = date_value

    def format_date(self, format_str):
        return self.date_value.strftime(format_str)


class SpecialCharacter:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Options:
    def __init__(self):
        self.special_characters_list = []
        self.nb_special_characters = 0

    def add_special_character(self, special_char):
        self.special_characters_list.append(special_char)

    def set_nb_special_characters(self, count):
        self.nb_special_characters = count


class CombinationGenerator:
    def __init__(self):
        self.base_words = []
        self.date_values = []
        self.result = []
        self.options = Options()

    def run(self):
        self.get_base_words()
        self.get_date_values()
        self.process_base_words()
        self.process_dates()
        self.generate_combinations()
        self.display_results()

    def get_base_words(self):
        num_words = self.get_integer_input('How many base words?', 1, 100)
        for i in range(num_words):
            value = input(f'Enter base word #{i + 1}: ')
            self.base_words.append(Word(value))

    def get_date_values(self):
        add_dates = self.get_yes_no_input('Do you want to add dates?')
        if add_dates:
            num_dates = self.get_integer_input('How many dates?', 1, 100)
            for i in range(num_dates):
                date_str = input(f'Enter date #{i + 1} (dd/mm/yyyy): ')
                date_value = datetime.strptime(date_str, '%d/%m/%Y')
                self.date_values.append(Date(date_value))

    def process_base_words(self):
        lowercase = self.get_yes_no_input(
            'Do you want to convert your word to lowercase?')
        if lowercase:
            for word in self.base_words:
                self.base_words.append(Word(word.get_value().lower()))

    def process_dates(self):
        monthname = self.get_yes_no_input('Do you want to convert month name?')
        if monthname:
            language = input('Which language? (en/fr/both): ')
            for date in self.date_values:
                self.base_words.append(Word(date.format_date('%B')))

        for date in self.date_values:
            self.result.append(date.format_date('dd-mm-yyyy'))
            self.result.append(date.format_date('mm-dd-yyyy'))
            self.result.append(date.format_date('yyyy-mm-dd'))

    def generate_combinations(self):
        result = [word.get_value() for word in self.base_words]

        special_characters_list = self.options.special_characters_list
        nb_special_characters = self.options.nb_special_characters

        for date in self.date_values:
            result.append(date.format_date('dd-mm-yyyy'))
            result.append(date.format_date('mm-dd-yyyy'))
            result.append(date.format_date('yyyy-mm-dd'))

        self.result = self.get_combinations(
            result, special_characters_list, nb_special_characters)

    def get_combinations(self, list1, list2, max_list2):
        combinations = []
        for i in range(2, min(5, len(list1) + len(list2)) + 1):
            for comb2 in self.combinations_with_replacement(list2, i - 1):
                for comb1 in self.combinations(list1, i - len(comb2)):
                    combinations.append(''.join(comb1 + comb2))
                    if len(combinations) >= max_list2:
                        return combinations
        return combinations

    def combinations(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)

    def combinations_with_replacement(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if not n and r:
            return
        indices = [0] * r
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)

    def display_results(self):
        print('Generated combinations:')
        for i, combination in enumerate(self.result, start=1):
            print(f'{i}. {combination}')

    @staticmethod
    def get_validated_input(message, validation_func):
        while True:
            user_input = input(message)
            if validation_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")

    @staticmethod
    def get_yes_no_input(message):
        def validation_func(user_input):
            return user_input.lower() in ['y', 'n']

        return CombinationGenerator.get_validated_input(f'{message} (y/n): ', validation_func).lower() == 'y'

    @staticmethod
    def get_integer_input(message, min_value, max_value):
        def validation_func(user_input):
            try:
                value = int(user_input)
                return min_value <= value <= max_value
            except ValueError:
                return False

        return int(CombinationGenerator.get_validated_input(f'{message} ({min_value}-{max_value}): ', validation_func))


if __name__ == "__main__":
    generator = CombinationGenerator()
    generator.run()
