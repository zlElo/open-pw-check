def score_eval(score):
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

    return improve, ranking