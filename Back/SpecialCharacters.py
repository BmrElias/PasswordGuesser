class SpecialCharacters:
    def __init__(self):
        self.common = ['.', '$', '?', '!', '*']
        self.allSpecialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*',
                                     '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']

    def getCommon(self):
        return self.common

    def getAll(self):
        return self.allSpecialCharacters
