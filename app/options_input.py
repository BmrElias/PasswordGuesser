class OptionsInput:
    @staticmethod
    def get_input(message):
        while True:
            try:
                value = input(message)
                return value
            except ValueError:
                print("Invalid input. Please try again.")

    @staticmethod
    def get_yes_no_input(message):
        while True:
            try:
                value = input(message)
                if value not in ["y", "n"]:
                    raise ValueError
                return value
            except ValueError:
                print("Invalid input. Please enter y or n.")

    @staticmethod
    def get_integer_input(message):
        while True:
            try:
                value = int(input(message))
                return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def get_language_input(message):
        while True:
            try:
                value = input(message)
                if value not in ["en", "fr", "both"]:
                    raise ValueError
                return value
            except ValueError:
                print("Invalid input. Please enter en, fr or both.")

    @staticmethod
    def get_special_chars_input(message):
        while True:
            try:
                value = input(message)
                if value not in ["all", "common", "none"]:
                    raise ValueError
                return value
            except ValueError:
                print("Invalid input. Please enter all or common.")
