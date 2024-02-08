import random
import string

def generate_password(length):
    if length < 8 or length > 20:
        raise ValueError("Password length must be between 8 and 20 characters.")
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = '!@#$%&*()_+=-'

    num_special_characters = length * 50 // 100
    num_letters = length * 30 // 100
    num_numbers = length * 20 // 100

    lowercase_part = ''.join(random.SystemRandom().choices(lowercase_letters, k=num_letters // 2))
    uppercase_part = ''.join(random.SystemRandom().choices(uppercase_letters, k=num_letters // 2))
    numbers_part = ''.join(random.SystemRandom().choices(numbers, k=num_numbers))
    special_characters_part = ''.join(random.SystemRandom().choices(special_characters, k=num_special_characters))

    password = lowercase_part + uppercase_part + numbers_part + special_characters_part

    shuffled_password = ''.join(random.SystemRandom().sample(password, len(password)))
    
    if len(shuffled_password) < length:
        shuffled_password += '*' * (length - len(shuffled_password))
    elif len(shuffled_password) > length:
        shuffled_password = shuffled_password[:length]

    return shuffled_password

try:
    length = int(input("Enter the desired password length (between 8 and 20): "))
    generated_password = generate_password(length)
    print("Generated password:", generated_password)
    print("Password length:", len(generated_password))
except ValueError as ve:
    print(ve)