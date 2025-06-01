def play_again(message):
    again = input(message)
    finish_loop = True
    while finish_loop:
        valid_yes_no = {"yes", "y", "no", "n"}
        if again.strip().lower() in valid_yes_no:
            finish_loop == False
            if again.strip().lower() == "yes" or again.strip().lower() == "y":
                return True
            else:
                return False
        else:
            again = input("I need a yes or no answer, please: ")
        
play = True
while play:
    palindrome = []
    validity_check = False
    while not validity_check:
        og_phrase = input("Let's see if you know any palindromes!\nEnter a word or sentence:")
        trimmed_lowered_phrase = og_phrase.strip().lower()
        if og_phrase.strip() == "":
            print("You can't enter nothing! Test your brain power, chicken!")
        else:
            list_phrase = list(trimmed_lowered_phrase)
            non_standard_check = [item for item in list_phrase if item != " "]
            for character in non_standard_check:
                if character.isalpha():
                    validity_check = True
                else:
                    validity_check = False
                    print("We are only checking letters and spaces! No punctuation, special characters, or numbers please!")
                    break
                
    for i in range(len(non_standard_check)):
        j = i + 1
        palindrome.append(non_standard_check[-j])
    if non_standard_check == palindrome:
        finish_loop = True
        message = "Congrats! '" + og_phrase + "' is a palindrome! Smarty-pants! Would you like to play again?\n"
        play = play_again(message)
    else:
        finish_loop = True
        message = "Ah, pooy, '" + og_phrase + "' is not a palindrome! Better luck next time. Would you like to play again?\n"
        play = play_again(message)
