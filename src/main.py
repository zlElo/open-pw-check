import re
import string
from funcs.score_val import score_eval
from funcs.cracking_test import cracking_test


def check():
    score = 0
    improve = ''
    ranking = ''
    information = ''
    cracked = 'no cracking test under 5 characters'
    password = input('Please enter your password here: ')
    
    listing_big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    listing_small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listing_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    listing_specials = ['!', '?', '"', ',', '.', '-', '_', '#', '(', ')', '{', '}', '$', '%', '<', '>', ';', ':', '+', '*', '~', '|', '@', '^', '°', '€', 'µ', '§', '³', '=', '`', 'ü', 'Ü', 'Ö', 'ö', 'Ä', 'ä']

    for i in listing_big_letters:
        if i in password:
            score += 1

    for i in listing_small_letters:
        if i in password:
            score += 1

    for i in listing_numbers:
        if i in password:
            score += 1

    for i in listing_specials:
        if i in password:
            score += 2
    
    print('[log] detection of used characters')

    length = len(password)

    if length < 5:
        score -= 1
        print('[log] detected too short password')
        print('[log] try to crack the password, this may takes a while!\n\n')
        print('[log] started')

        letters = re.search('[a-zA-Z]', password)

        letters = re.search('[a-zA-Z]', password)
        numbers = re.search('[1-9]', password)
        specials = re.search("[, !, ?, ., -, _, #, (, ), {, $, }, %, <, >, ;, :, +, *, ~, |, @, ^, °, €, µ, §, =, `, ü, Ü, Ö, ö, Ä, ä, ', ³]", password)

        numbers_ = string.digits
        letters_ = string.ascii_letters
        specials_ = "!?.-_#(){$}%<>;:+*~|@^°€µ§=`üÜÖöÄä'³"

        # stringbuilder
        uses_list = []

        if letters:
            uses_list.append(letters_)
        if numbers:
            uses_list.append(numbers_)
        if specials:
            uses_list.append(specials_)
        
        # Test for cracking the password
        generated = cracking_test(uses_list, length, password)

        # Set "cracked" var
        if generated == password:
            cracked = 'password was cracked with cracking tool!'
            print('[log] it was possible to crack the password')
        else:
            cracked = 'The password cracker wasnt able to crack your password!'
            print('[log] it was not possible to crack the password with 3.000.000 trys!')

    print('[log] check length')

    # Set length information
    if length < 11:
        information = 'password is long enough'
        score += 1

    if length >= 11:
        information = 'password is very long'
        score += 1

    if length < 7:
        information = 'password is too short'
        score -= 1

    print('[log] length check successfully')

    # check if password is in compromised list
    print('[log] compromised password check')
    with open('src/lists/list_compromised.txt') as file:
        content_ = file.read()
        if password in content_:
            compromised = 'your password is compromised!'
            print('[log] password compromised')
        else:
            compromised = 'your password isnt compromised!'
            print('[log] not compromised')

    # get ranking stats via score
    improve, ranking = score_eval(score)

    # Show stats
    print(f'\n\n-----Stats-----')
    print(f'\nScore: {score}\nRanking: {ranking}\nInformation: {information}\nCompromised: {compromised}\nCracked: {cracked}\nWhat can you make better?: {improve}')

if "__main__" in __name__:
    check()