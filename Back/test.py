import datetime

date_value = datetime.datetime.now()

words = ['Aà', 'bb', 'éè']

words_uppercase = []
words_camelcase = []
words_combinated = []
words_without_accent = []

words_leet = []

words_year_combinated = []
words_month_combinated = []
words_monthname_combinated = []
words_day_combinated = []


result = []


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


def month_name(month):
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


lowercase = input('Do you want to convert your word to lowercase? (y/n) ')
if lowercase == 'y':
    for idx in range(len(words)):
        words[idx] = words[idx].lower()

accents = input('Do you want to remove accents? (y/n) ')
if accents == 'y':
    for idx in range(len(words)):
        words[idx] = remove_accents(words[idx])

uppercase = input('Do you want to convert your word to uppercase? (y/n) ')
if uppercase == 'y':
    for word in words:
        words_uppercase.append(word.upper())
    words.extend(words_uppercase)

camelcase = input('Do you want to convert your word to camelcase? (y/n) ')
if camelcase == 'y':
    for word in words:
        words_camelcase.append(word.capitalize())
    words.extend(words_camelcase)

leet = input('Do you want to convert your word to leet speak? (y/n) ')
if leet == 'y':
    for word in words:
        words_leet.append(leet_speak(word))
    words.extend(words_leet)

monthname = input('Do you want to convert month name? (y/n) ')
if monthname == 'y':
    for idx in range(0, len(words)):
        words_day_combinated.append(
            words[idx] + month_name(date_value.strftime('%m')))
        words_day_combinated.append(month_name(
            date_value.strftime('%m')) + words[idx])
    words.extend(words_monthname_combinated)


# print("words : ", words)

for idx in range(0, len(words)):
    for idx2 in range(0, len(words)):
        if idx != idx2:
            words_combinated.append(words[idx] + words[idx2])

# print("combinaisons des mots : ", words_combinated)

for idx in range(0, len(words)):
    words_year_combinated.append(words[idx] + str(date_value.year))
    words_year_combinated.append(str(date_value.year) + words[idx])

# print("combinaisons des mots avec l'année : ", words_year_combinated)

for idx in range(0, len(words)):
    words_month_combinated.append(words[idx] + str(date_value.month))
    words_month_combinated.append(str(date_value.month) + words[idx])

# print("combinaisons des mots avec le mois : ", words_month_combinated)

for idx in range(0, len(words)):
    words_day_combinated.append(words[idx] + str(date_value.day))
    words_day_combinated.append(str(date_value.day) + words[idx])

# print("combinaisons des mots avec le jour : ", words_day_combinated)


result = words + words_uppercase + words_combinated + words_year_combinated + \
    words_month_combinated + words_monthname_combinated + \
    words_day_combinated + words_leet

print("résultat : ", result)
