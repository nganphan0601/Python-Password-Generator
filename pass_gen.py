import random
import string



def get_length():

        try:
            length = int(input("Enter the password length: "))
            while length < 12:
                print("A good password should be at least 12 characters")
                length = int(input("Enter the password length: "))
            
            return length
                
        except:
            print("Int Numbers only.")
            length = int(input("Enter the password length: "))
            return None


def password_generator(length):
# store characters in lists
    letter_list = list(string.ascii_lowercase + string.ascii_uppercase)
    digit_list = list(string.digits)
    symbol_list = list(string.punctuation)
    
# shuffle all lists to ensure randomness of characters
    for sub_list in [letter_list, digit_list, symbol_list]:
        random.shuffle(sub_list)

# 50% are letters, 25% are digits and 25% are symbol
    letter_chars = length // 2
    digit_chars = (length - letter_chars) // 2
    symbol_chars = length - (letter_chars + digit_chars)

    strong_pass = []

    strong_pass.append(random.sample(letter_list, letter_chars))
    strong_pass.append(random.sample(digit_list, digit_chars))
    strong_pass.append(random.sample(symbol_list, symbol_chars))


# shuffle the new pass
    random.shuffle(strong_pass)
    result = ''.join([''.join(sublist) for sublist in strong_pass])
    return result
    
user_length = get_length()
password = password_generator(user_length)
print(password)