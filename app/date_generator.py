from datetime import datetime


class Date:
    def __init__(self, date_input):
        self.date_value = datetime.strptime(date_input, "%d/%m/%Y")

    def get_formatted_date(self, format_str):
        return self.date_value.strftime(format_str)

    def get_month_name(self, language):
        month_names = {
            "en": {
                "1": "January",
                "2": "February",
                "3": "March",
                "4": "April",
                "5": "May",
                "6": "June",
                "7": "July",
                "8": "August",
                "9": "September",
                "10": "October",
                "11": "November",
                "12": "December",
            },
            "fr": {
                "1": "janvier",
                "2": "février",
                "3": "mars",
                "4": "avril",
                "5": "mai",
                "6": "juin",
                "7": "juillet",
                "8": "août",
                "9": "septembre",
                "10": "octobre",
                "11": "novembre",
                "12": "décembre",
            },
        }

        result = []
        month = str(self.date_value.month)

        if language in month_names:
            result.append(month_names[language][month])
        elif language == "both":
            result.append(month_names["en"][month])
            result.append(month_names["fr"][month])

        return result
