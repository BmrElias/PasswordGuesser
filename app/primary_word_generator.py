from generator_interface import GeneratorInterface
from options_input import OptionsInput
from word import Word


class PrimaryWordsGenerator(GeneratorInterface):
    def __init__(self, base_words):
        self.base_words = base_words
        self.primary_words = []

    def generate(self):
        lowercase = OptionsInput.get_yes_no_input(
            "Do you want to convert your word to lowercase? (y/n) "
        )
        if lowercase == "y":
            for word in self.base_words:
                self.primary_words.append(Word(word).convert_to_lowercase())
        pass

    def get_primary_words(self):
        return self.primary_words
