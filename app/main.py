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
        self.special_characters_list = []
        self.nb_special_characters = 0

    def run(self):
        self.get_base_words()
        self.get_date_values()
        self.generate_results()

    def get_base_words(self):
        words_input = OptionsInput.get_input(
            "Enter base words separated by spaces: ")
        self.base_words = words_input.split()

    def get_date_values(self):
        add_dates = OptionsInput.get_yes_no_input(
            "Do you want to add dates? (y/n) ")
        if add_dates == "y":
            num_dates = OptionsInput.get_integer_input("How many dates? ")
            for i in range(num_dates):
                date_input = OptionsInput.get_input(
                    "Enter date (dd/mm/yyyy): ")
                date = Date(date_input)
                self.date_values.append(date)
            self.generate_month_name_results()

    def generate_results(self):
        self.generate_date_results()
        primary_words_generator = PrimaryWordsGenerator(self.base_words)
        primary_words_generator.generate()
        self.primary_words = primary_words_generator.get_primary_words()
        self.generate_leet_speak_results()
        self.generate_special_characters_results()
        self.generate_combinations(
            self.result, self.special_characters_list, self.nb_special_characters
        )

    def generate_date_results(self):
        date_formats = ["%d-%m-%Y", "%Y-%m-%d", "%m-%Y", "%Y", "%m", "%d"]
        self.result.extend([date.get_formatted_date(fmt)
                            for date in self.date_values for fmt in date_formats])

    def generate_month_name_results(self):
        monthname = OptionsInput.get_yes_no_input(
            "Do you want to convert month name? (y/n) ")
        if monthname == "y":
            language = OptionsInput.get_language_input(
                "Which language? (en/fr/both) ")
            self.base_words.extend(
                [name for date in self.date_values for name in date.get_month_name(language)])
            self.generate_date_results()
            self.result.extend([date.get_formatted_date("%y")
                                for date in self.date_values])

    def generate_leet_speak_results(self):
        leet_speak_generator = LeetSpeakGenerator(self.primary_words)
        leet_speak_generator.generate()
        self.result.extend(leet_speak_generator.get_result())

    def generate_special_characters_results(self):
        special_chars = OptionsInput.get_yes_no_input(
            "Do you want to add special characters? (y/n) ")
        if special_chars == "y":
            special_chars = OptionsInput.get_special_chars_input(
                "Do you want to add all special characters or common ones? (all/common) "
            )
            self.special_characters_list = SpecialCharacters.add_special_characters(
                special_chars)
            if self.special_characters_list:
                self.nb_special_characters = OptionsInput.get_integer_input(
                    "How many special characters do you want to add? (0-3) "
                )
                if self.nb_special_characters < 0:
                    self.nb_special_characters = 0
                elif self.nb_special_characters > 3:
                    self.nb_special_characters = 3
            else:
                self.nb_special_characters = 0

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


if __name__ == "__main__":
    main = Main()
    main.run()
