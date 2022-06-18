from datetime import datetime


def check_age(value):
    current_date = datetime.now()
    birthday = datetime.strptime(value, '%d.%m.%Y')
    checking_age = current_date.year - birthday.year
    if checking_age >= 100:
        raise Exception(
            f'Hey, grandpa! You are too old) Check if you have entered correct birthday date.')
    elif current_date <= birthday:
        raise Exception(
            f'Hey, baby! You are too young) Check if you have entered correct birthday date.')
    else:
        return True


