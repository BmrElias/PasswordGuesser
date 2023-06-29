class SpecialCharacters:
    @staticmethod
    def add_special_characters(special_chars):
        if special_chars == "all":
            return [
                "!",
                "@",
                "#",
                "$",
                "%",
                "^",
                "&",
                "*",
                "(",
                ")",
                "-",
                "_",
                "=",
                "+",
                "[",
                "]",
                "{",
                "}",
                "|",
                "\\",
                ";",
                ":",
                '"',
                "'",
                ",",
                "<",
                ".",
                ">",
                "/",
                "?",
            ]
        elif special_chars == "common":
            return [".", "$", "?", "!"]
        return []
