class Word:
    def __init__(self):
        self.words = []
        self.words_uppercase = []
        self.words_camelcase = []
        self.words_leet = []
        self.words_without_accent = []
        self.wordsPossibilities = []

    def leet_speak(word):
        word = word.replace('a', '4')
        word = word.replace('e', '3')
        word = word.replace('i', '1')
        word = word.replace('o', '0')
        word = word.replace('l', '1')
        word = word.replace('s', '5')
        word = word.replace('b', '8')
        word = word.replace('t', '7')
        word = word.replace('z', '2')
        word = word.replace('g', '6')
        return word

    def remove_accents(word):
        word = word.replace('é', 'e')
        word = word.replace('è', 'e')
        word = word.replace('ê', 'e')
        word = word.replace('à', 'a')
        word = word.replace('â', 'a')
        word = word.replace('ù', 'u')
        word = word.replace('û', 'u')
        word = word.replace('î', 'i')
        word = word.replace('ï', 'i')
        word = word.replace('ô', 'o')
        word = word.replace('ö', 'o')
        word = word.replace('ç', 'c')
        return word

    def upper_case(self):
        for word in self.words:
            self.words_uppercase.append(word.upper())

    def camel_case(self):
        for word in self.words:
            self.words_camelcase.append(word.capitalize())

    def lower_case(self):
        for word in self.words:
            self.words_lower.append(word.lower())

    def leet_speak(self):
        for word in self.words:
            self.words_leet.append(self.leet_speak(word))

    def without_accent(self):
        for word in self.words:
            self.words_without_accent.append(self.remove_accents(word))

    def possibilities(self):
        self.wordsPossibilities = self.words + self.words_uppercase + \
            self.words_camelcase + self.words_leet + self.words_without_accent
