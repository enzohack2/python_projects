import string, random


def generate_random_password():
    """
    Generates random 8 character password.
    source: https://geekflare.com/password-generator-python-code/
    """
       
    ## characters to generate password from
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#£&*")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    ## length of password from the user
    length = 8

    ## number of character types
    alphabets_count = 5
    digits_count = 2
    special_characters_count = 1

    characters_count = alphabets_count + digits_count + special_characters_count

    ## initializing the password
    password = []
    
    ## picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))


    ## picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))


    ## picking random alphabets
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))


    ## if the total characters count is less than the password length
    ## add random characters to make it equal to the length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))


    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    final_password = "".join(password)
    return final_password
