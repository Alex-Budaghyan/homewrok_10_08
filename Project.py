def Email():
    email = input("Enter an email: ").strip()
    if email.endswith('@gmail.com') and email.isascii():
        print('The email is valid')
    else:
        print("The email is not valid")


def Website_URL():
    url = input('Enter an url: ').strip()
    if url.startswith('https://www.', 'http://www.') and len(url) < 2270 and '.com/' in url and url.isascii():
        print('The website URL is valid')
    else:
        print('The website URL is not valid')


def Date():
    date = input('Enter the date: ').strip()
    if date[2] == date[5] in ('-', '/', ' '):
        print('The date is valid')
    else:
        print('The date is not valid')


def Number():
    number = input('Enter the number: ')
    if number.isdigit():
        print("The number is valid")
    else:
        print("The number is not valid")


def Credit_card_number():
    num = input('Enter the credit card number: ')
    if num.isdigit() and len(num) == 16:
        print('The credit card number is valid')
    else:
        print('The credit card number is not valid')


def Mobile_phone_number():
    phone_num = input('Enter the phone number: ')
    if ((phone_num.startswith('+374') and len(phone_num) == 12 and phone_num[1:].isdigit()) or
            phone_num.startswith('0') and len(phone_num) == 9 and phone_num.isdigit()):
        print('The phone number is valid')
    else:
        print('The phone number is not valid')


try:
    opt = int(input("Input an option: "))
except:
    print("The option must be an integer from 1 to 6")


if opt == 1:
    Email()
elif opt == 2:
    Website_URL()
elif opt == 3:
    Date()
elif opt == 4:
    Number()
elif opt == 5:
    Credit_card_number()
elif opt == 6:
    Mobile_phone_number()
else:
    print("The option must be an integer from 1 to 6")
