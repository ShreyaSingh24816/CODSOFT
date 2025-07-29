import random
import string

def password_generator():
    letter=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    print("-----Welcome to password generator-----")

    total_lenth=int(input("Enter total length of the password: "))
    letter_number=int(input("Enter how many letters you want in your password: "))
    digit_number=int(input("Enter the number of digits you want to use in your password: "))
    special_number=int(input("Enter the number of special character you want to use in your password: "))
    if letter_number + digit_number + special_number != total_lenth:
        print("Error: The sum of letters, digits, and special characters must be equal to the total password length!")
        return
    
    password=""
    for i in range(1,letter_number+1):
        char=random.choice(letter)
        password+=char
    for i in range(1,digit_number+1):
        dig=random.choice(digits)
        password+=dig
    for i in range(1,special_number+1):
        spec=random.choice(special)
        password+=spec
    password_list=list(password)
    random.shuffle(password_list)
    generate_password = ''.join(password_list)
    print("Generated Password:", generate_password)

password_generator()