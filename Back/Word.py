class Word:

    @staticmethod
    def leet_speak(word):
        leet_chars = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            'l': '1',
            's': '5',
            'b': '8',
            't': '7',
            'z': '2',
            'g': '6'
        }
        for leet_char, replacement_char in leet_chars.items():
            word = word.replace(leet_char, replacement_char)
        return word

    @staticmethod
    def remove_accents(word):
        accents = {
            'é': 'e',
            'è': 'e',
            'ê': 'e',
            'à': 'a',
            'â': 'a',
            'ù': 'u',
            'û': 'u',
            'î': 'i',
            'ï': 'i',
            'ô': 'o',
            'ö': 'o',
            'ç': 'c'
        }
        for accented_char, replacement_char in accents.items():
            word = word.replace(accented_char, replacement_char)
        return word
