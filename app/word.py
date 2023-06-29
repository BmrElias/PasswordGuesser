class Word:
    def __init__(self, word):
        self.word = word

    def convert_to_lowercase(self):
        return self.word.lower()

    def convert_to_uppercase(self):
        return self.word.upper()

    def convert_to_camelcase(self):
        return self.word.capitalize()

    def remove_accents(self):
        accented_chars = {
            "é": "e",
            "è": "e",
            "ê": "e",
            "à": "a",
            "â": "a",
            "ù": "u",
            "û": "u",
            "î": "i",
            "ï": "i",
            "ô": "o",
            "ö": "o",
            "ç": "c",
        }
        new_word = ""
        for char in self.word:
            if char in accented_chars:
                new_word += accented_chars[char]
            else:
                new_word += char
        return new_word
