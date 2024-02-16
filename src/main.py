import re
import secrets
import string
import sys


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
    
    print('[Log] detection of used characters')

    length = len(password)

    if length < 5:
        score -= 1
        print('[Log] detected too short password')
        print('[Log] try to crack the password, this may takes a while!\n\n')
        print('[Log] started')

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
        
        uses = ''.join(uses_list)
        generated = '123'
        count = 3000000
        count2 = 0

        print("Total count: "+str(count),end=' ')

        used_passwords = set()
        for i in range(count):
            while True:
                generated = ''.join(secrets.choice(uses) for i in range(int(length)))
                if generated not in used_passwords: 
                    used_passwords.add(generated)
                    break
            
            count2 += 1
            sys.stdout.flush()
            print("\rSteps try crack: " + str(i+1) + "/" + str(count) + ' ' + 'generated password: ' + generated, end=' ')
            if generated == password:
                break

        print("")#to change the current line

        if generated == password:
            cracked = 'password was cracked with cracking tool!'
            print('[Log] it was possible to crack the password')
        else:
            cracked = 'The password cracker wasnt able to crack your password!'
            print('[Log] it was not possible to crack the password with 3.000.000 trys!')

    print('[Log] check length')

    if length < 11:
        information = 'password is long enough'
        score += 1

    if length >= 11:
        information = 'password is very long'
        score += 1

    if length < 7:
        information = 'password is too short'
        score -= 1

    print('[Log] length check successfully')

    print('[Log] compromised password check')
    with open('src/lists/list_compromised.txt') as file:
        content_ = file.read()
        if password in content_:
            compromised = 'your password is compromised!'
            print('[Log] password compromised')
        else:
            compromised = 'your password isnt compromised!'
            print('[Log] not compromised')

    if score <= 5:
        improve = 'use a password with big and small letters, numbers and special symbols!'
        ranking = 'C- (bad)'

    if score == 6:
        improve = 'add more special symbols, small/big letters and numbers!'
        ranking = 'C- (bad)'

    if score == 7:
        improve = 'add more special symbols, small/big letters and numbers!'
        ranking = 'C (bad)'

    if score == 8:
        improve = 'add more special symbols, small/big letters and numbers!'
        ranking = 'C+ (not the best)'

    if score == 9:
        improve = 'try to add more special symbols, small/big letters and numbers!'
        ranking = 'B- (okay)'

    if score == 10:
        improve = 'your password is better, but add more/some special symbols, small/big letters and numbers!'
        ranking = 'B (better)'

    if score == 11:
        improve = 'your password is good, eventually you add more/some special symbols!'
        ranking = 'B+ (good)'

    if score == 12:
        improve = 'your password is good, eventually you add more/some special symbols!'
        ranking = 'A- (good)'

    if score == 13:
        improve = 'your password is very good, eventually you add more/some special symbols!'
        ranking = 'A (very good)'

    if score >= 14:
        improve = 'there is nothing what you can make better!'
        ranking = 'A+ (perfect)'

    # Show stats
    print(f'\n\n-----Stats-----')
    print(f'\nScore: {score}\nRanking: {ranking}\nInformation: {information}\nCompromised: {compromised}\nCracked: {cracked}\nWhat can you make better?: {improve}')

check()