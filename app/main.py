from datetime import datetime

from combinations_generator import CombinationsGenerator
from date_generator import Date
from leet_speak_generator import LeetSpeakGenerator
from options_input import OptionsInput
from primary_word_generator import PrimaryWordsGenerator
from special_characters import SpecialCharacters


class Main:
    def __init__(self):
        self.base_words = []
        self.date_values = []
        self.primary_words = []
        self.result = []

    def run(self):
        self.get_base_words()
        self.get_date_values()
        self.generate_results()

    def get_base_words(self):
        words_input = OptionsInput.get_input("Enter base words separated by spaces: ")
        self.base_words = words_input.split()

    def get_date_values(self):
        add_dates = OptionsInput.get_yes_no_input("Do you want to add dates? (y/n) ")
        if add_dates == "y":
            num_dates = OptionsInput.get_integer_input("How many dates? ")
            for i in range(num_dates):
                date_input = OptionsInput.get_input("Enter date (dd/mm/yyyy): ")
                date = Date(date_input)
                self.date_values.append(date)

    def generate_results(self):
        self.generate_date_results()
        self.generate_month_name_results()
        primary_words_generator = PrimaryWordsGenerator(self.base_words)
        primary_words_generator.generate()
        self.primary_words = primary_words_generator.get_primary_words()
        self.generate_leet_speak_results()
        self.generate_special_characters_results()
        self.print_results()

    def generate_date_results(self):
        for date in self.date_values:
            self.result.append(date.get_formatted_date("%d-%m-%Y"))
            self.result.append(date.get_formatted_date("%Y-%m-%d"))
            self.result.append(date.get_formatted_date("%m-%Y"))
            self.result.append(date.get_formatted_date("%Y"))
            self.result.append(date.get_formatted_date("%m"))
            self.result.append(date.get_formatted_date("%d"))

    def generate_month_name_results(self):
        monthname = OptionsInput.get_yes_no_input(
            "Do you want to convert month name? (y/n) "
        )
        if monthname == "y":
            language = OptionsInput.get_language_input("Which language? (en/fr/both) ")
            for date in self.date_values:
                self.base_words.extend(date.get_month_name(language))
                self.result.append(date.get_formatted_date("%d-%m-%Y"))
                self.result.append(date.get_formatted_date("%Y-%m-%d"))
                self.result.append(date.get_formatted_date("%m-%Y"))
                self.result.append(date.get_formatted_date("%Y"))
                self.result.append(date.get_formatted_date("%y"))
                self.result.append(date.get_formatted_date("%m"))
                self.result.append(date.get_formatted_date("%d"))

    def generate_leet_speak_results(self):
        leet_speak_generator = LeetSpeakGenerator(self.primary_words)
        leet_speak_generator.generate()
        self.result.extend(leet_speak_generator.get_result())

    def generate_special_characters_results(self):
        special_characters_list = SpecialCharacters.add_special_characters(
            self.get_special_characters()
        )
        if special_characters_list:
            nb_special_characters = OptionsInput.get_integer_input(
                "How many special characters do you want to add? (0-3) "
            )
            if nb_special_characters < 0:
                nb_special_characters = 0
            elif nb_special_characters > 3:
                nb_special_characters = 3
        else:
            nb_special_characters = 0

        self.generate_combinations(
            self.result, special_characters_list, nb_special_characters
        )

    def get_special_characters(self):
        special_chars = OptionsInput.get_yes_no_input(
            "Do you want to add special characters? (y/n) "
        )
        if special_chars == "y":
            special_chars = OptionsInput.get_special_chars_input(
                "Do you want to add all special characters or common ones? (all/common) "
            )
            return special_chars
        return ""

    def replace_chars(self, char_type, word):
        char_dict = {
            "maj_leet": {
                "a": "4",
                "e": "3",
                "i": "1",
                "o": "0",
                "l": "1",
                "s": "5",
                "b": "8",
                "t": "7",
                "z": "2",
                "g": "6",
            },
        }

        if char_type not in char_dict:
            return [word]

        all_combinations = [[]]
        for char in word:
            new_combinations = []
            if char.lower() in char_dict[char_type]:
                for combo in all_combinations:
                    new_combinations.append(combo + [char])
                    new_combinations.append(
                        combo + [char_dict[char_type][char.lower()]]
                    )
            else:
                for combo in all_combinations:
                    new_combinations.append(combo + [char])
            all_combinations = new_combinations

        replaced_words = []
        for combination in all_combinations:
            replaced_words.append("".join(combination))

        return replaced_words

    def generate_combinations(self, list1, list2, max_list2):
        count = 0
        start_time = datetime.now()

        for i in range(2, min(5, len(list1) + len(list2)) + 1):
            for comb2_len in range(min(i, len(list2)) + 1):
                for comb2 in CombinationsGenerator.combinations_with_replacement(
                    list2, comb2_len
                ):
                    comb1_len = i - comb2_len
                    for comb1 in CombinationsGenerator.permutations_with_replacement(
                        list1, comb1_len
                    ):
                        num_list2 = sum(1 for x in comb1 + comb2 if x in list2)
                        if num_list2 <= max_list2:
                            combination = "".join(comb1 + comb2)
                            print(combination)
                            count += 1

        duration = datetime.now() - start_time
        print("Nombre de résultats: " + str(count))
        print("Temps de calcul: " + str(duration))

    def print_results(self):
        for result in self.result:
            print(result)


if __name__ == "__main__":
    main = Main()
    main.run()
