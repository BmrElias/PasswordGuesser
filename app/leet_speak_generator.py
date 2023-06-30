from generator_interface import GeneratorInterface
from options_input import OptionsInput


class LeetSpeakGenerator(GeneratorInterface):
    def __init__(self, primary_words):
        self.primary_words = primary_words
        self.result = []

    def generate(self):
        leet = OptionsInput.get_yes_no_input(
            "Do you want to convert your word to leet speak? (y/n) "
        )
        if leet == "y":
            for word in self.primary_words:
                self.result.extend(self.replace_chars("leet", word))
        else:
            self.result = self.primary_words

        pass

    def replace_chars(self, char_type, word):
        char_dict = {
            "leet": {
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

    def get_result(self):
        return self.result
