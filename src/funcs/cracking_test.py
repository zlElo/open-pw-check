import secrets
import sys

def cracking_test(uses_list, length, password):
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

    print("") # to change the current line
    return generated