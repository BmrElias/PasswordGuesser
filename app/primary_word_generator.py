from generator_interface import GeneratorInterface
from options_input import OptionsInput
from word import Word


class PrimaryWordsGenerator(GeneratorInterface):
    def __init__(self, base_words):
        self.base_words = base_words
        self.primary_words = []

    def add_base_words_to_primary_words(self):
        for word in self.base_words:
            self.primary_words.append(word)

    def generate(self):

        self.add_base_words_to_primary_words()

        lowercase = OptionsInput.get_yes_no_input(
            "Do you want to convert your word to lowercase? (y/n) "
        )
        if lowercase == "y":
            for word in self.base_words:
                self.primary_words.append(Word(word).convert_to_lowercase())

        uppercase = OptionsInput.get_yes_no_input(
            "Do you want to convert your word to uppercase? (y/n) "
        )
        if uppercase == "y":
            for word in self.base_words:
                self.primary_words.append(Word(word).convert_to_uppercase())

        camelcase = OptionsInput.get_yes_no_input(
            "Do you want to convert your word to camelcase? (y/n) "
        )
        if camelcase == "y":
            for word in self.base_words:
                self.primary_words.append(Word(word).convert_to_camelcase())

        remove_accents = OptionsInput.get_yes_no_input(
            "Do you want to remove accents? (y/n) "
        )
        if remove_accents == "y":
            for word in self.base_words:
                self.primary_words.append(Word(word).remove_accents())

        pass

    def get_primary_words(self):
        return self.primary_words
