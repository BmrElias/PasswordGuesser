class Date:
    def __init__(self):
        self.dates = []
        self.datesPossibilities = []

    def getDay(self, date):
        return date.split('/')[0]

    def getMonth(self, date):
        return date.split('/')[1]

    def getYear(self, date):
        return date.split('/')[2]

    def getMonthName(self, date):
        month = self.getMonth(date)
        month = month.replace('01', 'janvier')
        month = month.replace('02', 'fevrier')
        month = month.replace('03', 'mars')
        month = month.replace('04', 'avril')
        month = month.replace('05', 'mai')
        month = month.replace('06', 'juin')
        month = month.replace('07', 'juillet')
        month = month.replace('08', 'aout')
        month = month.replace('09', 'septembre')
        month = month.replace('10', 'octobre')
        month = month.replace('11', 'novembre')
        month = month.replace('12', 'decembre')
        return month

    def twoDigitYear(self, date):
        return date[2:]

    