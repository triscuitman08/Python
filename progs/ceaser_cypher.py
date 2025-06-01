def encrypt():
    text = input("Cheerio! Let's make your message UNREADABLE! (Except to anybody over the age of 10...)\nEnter your message here: ")
    is_num_num = False
    while not is_num_num:
        try:
            user_number = input("Cherrio! And what would you like your shift value to be? ")
            shift = int(user_number)
            if shift < 1 or shift > 25:
                print(f"'{user_number}' is not a valid shift value! You must use whole numbers between 1 and 25")
            else:
                is_num_num = True
        except ValueError:
            try:
                float(user_number)
                print("Shift Values must be between whole number integers between 1 and 25")
            except ValueError:
                print("We need ONLY numbers, silly goose!")
                
    cipher = ''
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            # Encrypt uppercase characters
            if char.isupper():
                cipher += chr((ord(char) + shift - 65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                cipher += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher += char
    return cipher

def decrypt():
    text = input("Sounds like a smashing good time! Lets unhack the hackable!\n What message would you like decrypted? ")
    is_num_num = False
    while not is_num_num:
        try:
            user_number = input("Cherrio! And what would you like your shift value to be? ")
            shift = int(user_number)
            if shift < 1 or shift > 25:
                print(f"'{user_number}' is not a valid shift value! You must use whole numbers between 1 and 25")
            else:
                is_num_num = True
        except ValueError:
            try:
                float(user_number)
                print("Shift Values must be between whole number integers between 1 and 25")
            except ValueError:
                print("We need ONLY numbers, silly goose!")
    unencrypted = ''
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            # Decrypt uppercase characters
            if char.isupper():
                unencrypted += chr((ord(char) - shift - 65) % 26 + 65)
            
            # Decrypt lowercase Characters
            else:
                unencrypted += chr((ord(char) - shift - 97) % 26 + 97)  
        else:
            unencrypted += char          
    return unencrypted

choice_bool = False
while choice_bool != True:
    choice = input("Would you like to encrypt or decrypt a message?\n")
    if choice.lower() == "decrypt" or choice.lower() == "encrypt":
        choice_bool = True
    else:
        print("I'm terribly sorry old chap, but I did not understand that, please enter 'Decrypt' or 'Encrypt'.")
    
if choice.lower() == "encrypt":
    print(encrypt())
elif choice.lower() == "decrypt":
    print(decrypt())
else:
    print("I'm not really sure how you tricked my error logic, but congrats, have a cookie....")