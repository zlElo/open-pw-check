import re

password = '123'

letters = re.search('[a-zA-Z]', password)
numbers = re.search('[1-9]', password)
specials = re.search("[, !, ?, ., -, _, #, (, ), {, $, }, %, <, >, ;, :, +, *, ~, |, @, ^, °, €, µ, §, =, `, ü, Ü, Ö, ö, Ä, ä, ', ³]", password)


if letters == None:
    print('hasnt letters')
else:
    print('has letters')

if numbers == None:
    print('hasnt numbers')
else:
    print('has numbers')

if specials == None:
    print('hasnt specials')
else:
    print('has specials')