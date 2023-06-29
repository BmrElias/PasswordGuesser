from datetime import datetime


def replace_chars(char_type, word):
    char_dict = {
        'leet': {
            'a': '4', 'e': '3', 'i': '1', 'o': '0', 'l': '1', 's': '5', 'b': '8', 't': '7', 'z': '2', 'g': '6'
        },
        'accent': {
            'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'ç': 'c'
        },
        'maj_accent': {
            'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Ç': 'C'
        },
        'maj_leet': {
            'A': '4', 'E': '3', 'I': '1', 'O': '0', 'L': '1', 'S': '5', 'B': '8', 'T': '7', 'Z': '2', 'G': '6'
        },
    }

    if char_type not in char_dict:
        return [word]

    all_combinations = [[]]
    for char in word:
        if char.lower() in char_dict[char_type]:
            new_combinations = []
            for combo in all_combinations:
                new_combinations.append(combo + [char])
                new_combinations.append(
                    combo + [char_dict[char_type][char.lower()]])
            all_combinations = new_combinations
        else:
            for combo in all_combinations:
                combo.append(char)

    replaced_words = []
    for combination in all_combinations:
        replaced_words.append(''.join(combination))

    return replaced_words


def month_name(language, date):
    month_names = {
        'en': {
            '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'
        },
        'fr': {
            '1': 'janvier', '2': 'février', '3': 'mars', '4': 'avril', '5': 'mai', '6': 'juin', '7': 'juillet', '8': 'août', '9': 'septembre', '10': 'octobre', '11': 'novembre', '12': 'décembre'
        }
    }

    toReturn = []

    month = str(date.month)

    if language in month_names:
        toReturn.append(month_names[language][month])
    elif language == 'both':
        toReturn.append(month_names['en'][month])
        toReturn.append(month_names['fr'][month])
    else:
        return

    return toReturn


def special_characters():
    special_chars = input('Do you want to add special characters? (y/n) ')
    if special_chars == 'y':
        special_chars = input(
            'Do you want to add all special characters or common ones? (all/common) ')
        return add_special_characters(special_chars)
    return []


def add_special_characters(special_chars):
    if special_chars == 'all':
        return ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?']
    elif special_chars == 'common':
        return ['.', '$', '?',        '!', '*']
    return []


def generate_combinations(list1, list2, max_list2):
    count = 0
    start_time = datetime.now()

    combinations = set()

    for i in range(2, min(5, len(list1) + len(list2)) + 1):
        for comb2_len in range(min(i, len(list2)) + 1):
            for comb2 in combinations_with_replacement(list2, comb2_len):
                comb1_len = i - comb2_len
                for comb1 in permutations_with_replacement(list1, comb1_len):
                    num_list2 = sum(1 for x in comb1 + comb2 if x in list2)
                    if num_list2 <= max_list2:
                        combination = ''.join(comb1 + comb2)
                        # Ajouter la combinaison à l'ensemble
                        combinations.add(combination)

    for combination in combinations:
        print(combination)
        count += 1

    duration = datetime.now() - start_time
    print('Nombre de résultats: ' + str(count))
    print('Temps de calcul: ' + str(duration))


def combinations_with_replacement(lst, k):
    if k == 0:
        yield []
    else:
        for i, item in enumerate(lst):
            for combo in combinations_with_replacement(lst[i:], k - 1):
                yield [item] + combo


def permutations_with_replacement(lst, k):
    if k == 0:
        yield []
    else:
        for i in range(len(lst)):
            for combo in permutations_with_replacement(lst, k - 1):
                yield [lst[i]] + combo


base_words = input('Enter base words separated by spaces: ').split()
num_date = input('Do you want to add dates? (y/n) ')
if num_date == 'y':
    num_date = int(input('How many dates? '))
    date_value = []
    for i in range(num_date):
        date = input('Enter date (dd/mm/yyyy): ')
        date_value.append(datetime.strptime(date, '%d/%m/%Y'))
else:
    date_value = []


primary_words = base_words.copy()
result = []

for date in date_value:
    result.append(str(date.day) + '-' +
                  str(date.month) + '-' + str(date.year))
    result.append(str(date.year) + '-' +
                  str(date.month) + '-' + str(date.day))
    result.append(str(date.month) + '-' + str(date.year))
    result.append(str(date.year))
    result.append(str(date.month))
    result.append(str(date.day))
monthname = input('Do you want to convert month name? (y/n) ')
if monthname == 'y':
    language = input('Which language? (en/fr/both) ')
    for date in date_value:
        base_words.extend(month_name(language, date))
        result.append(str(date.day) + '-' +
                      str(date.month) + '-' + str(date.year))
        result.append(str(date.year) + '-' +
                      str(date.month) + '-' + str(date.day))
        result.append(str(date.month) + '-' + str(date.year))
        result.append(str(date.year))
        result.append(str(date.year)[-2:])
        result.append(str(date.month))
        result.append(str(date.day))


lowercase = input('Do you want to convert your word to lowercase? (y/n) ')
if lowercase == 'y':
    for word in base_words:
        primary_words.append(word.lower())

accents = input('Do you want to remove accents? (y/n) ')
if accents == 'y':
    for word in base_words:
        primary_words.extend(replace_chars('accent', word))

uppercase = input('Do you want to convert your word to uppercase? (y/n) ')
if uppercase == 'y':
    for word in base_words:
        primary_words.append(word.upper())

camelcase = input('Do you want to convert your word to camelcase? (y/n) ')
if camelcase == 'y':
    for word in base_words:
        primary_words.append(word.capitalize())


primary_words = list(dict.fromkeys(primary_words))

result.extend(primary_words)


leet = input('Do you want to convert your word to leet speak? (y/n) ')
if leet == 'y':
    for word in primary_words:
        result.extend(replace_chars('leet', word))

if uppercase == 'y' and accents == 'y':
    for word in primary_words:
        result.extend(replace_chars('maj_accent', word))
if uppercase == 'y' and leet == 'y':
    for word in primary_words:
        result.extend(replace_chars('maj_leet', word))


special_characters_list = special_characters()


if special_characters_list:
    nb_special_characters = int(input(
        'How many special characters do you want to add? (0-3) '))
    if nb_special_characters < 0:
        nb_special_characters = 0
    elif nb_special_characters > 3:
        nb_special_characters = 3
else:
    nb_special_characters = 0

generate_combinations(result, special_characters_list, nb_special_characters)
