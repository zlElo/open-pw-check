# open-pw-check
Open-pw-check is a OpenSource password checker - private without datas!


## What you need to install
- Python (3)

## How to use
1. clone repository ```git clone https://github.com/zlElo/open-pw-check.git```
2. go to src folder
3. run ```python3 main.py``` or for windows double click on main.py file

## Information for the cracking tool
The program has a little cracking tool integrated. If the password has >5 characters, the program will try to crack the password with random characters with the lentgh of the password. Which characters?:
- if password has letters = letters
- if password has numbers = numbers
- if password has specials = specials
The program will detect which characters are used (letters, numbers or specials) and will use only this for cracking. For example:
- the password is following: ```h23d```
- open-pw-check detect that the password has numbers and letters
- now the program create passwords with 4 letters and numbers, for example: ```dwd1``` or ```ff5e```
- Now a comparison is made as to whether the generated password fits
