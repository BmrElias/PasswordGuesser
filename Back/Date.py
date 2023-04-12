import datetime


class Date:
    def __init__(self):
        self.value = datetime.datetime.now()

    def get_year(self, short=False):
        return self.value.strftime('%y' if short else '%Y')

    def get_month_number(self):
        return self.value.strftime('%m')

    def get_month_name(self, language='en'):
        month_names = {
            'en':
                {
                    '01': 'January',
                    '02': 'February',
                    '03': 'March',
                    '04': 'April',
                    '05': 'May',
                    '06': 'June',
                    '07': 'July',
                    '08': 'August',
                    '09': 'September',
                    '10': 'October',
                    '11': 'November',
                    '12': 'December'
                },
            'fr':
                {
                    '01': 'janvier',
                    '02': 'février',
                    '03': 'mars',
                    '04': 'avril',
                    '05': 'mai',
                    '06': 'juin',
                    '07': 'juillet',
                    '08': 'août',
                    '09': 'septembre',
                    '10': 'octobre',
                    '11': 'novembre',
                    '12': 'décembre'
                }
        }
        return month_names.get(language, {}).get(self.get_month_number(), self.get_month_number())

    def get_day(self):
        return self.value.strftime('%d')
