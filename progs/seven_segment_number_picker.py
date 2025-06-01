seven_seg = [
    # 0
    '''###
# #
# #
# #
###''',

    # 1
    '''  #
  #
  #
  #
  #''',

    # 2
    '''###
  #
###
#  
###''',

    # 3
    '''###
  #
###
  #
###''',

    # 4
    '''# #
# #
###
  #
  #''',

    # 5
    '''###
#  
###
  #
###''',

    # 6
    '''###
#  
###
# #
###''',

    # 7
    '''###
  #
  #
  #
  #''',

    # 8
    '''###
# #
###
# #
###''',

    # 9
    '''###
# #
###
  #
###'''
]

#Get a valid non-negative integer from the user
is_num_num = False
while not is_num_num:
    try:
        user_number = input("Input a non-negative integer: ")
        user_int = int(user_number)
        if user_int < 0:
            print(f"'{user_number}' is a negative number, silly goose! Positive, whole numbers only!")
        else:
            is_num_num = True
    except ValueError:
        try:
            float(user_number)
            print("Please input an integer value, or whole number, not a decimal value!")
        except ValueError:
            print("We need ONLY numbers, silly goose!")

#Split the input string into its individual characters, then convert to ints
string_list = list(user_number.strip())  
number_list = [int(s) for s in string_list]

#Create patterns row by row of each seven_seg element
patterns = [seven_seg[d].split("\n") for d in number_list]

#Print row-by-row, stitching each digit’s row together
# There are exactly 5 rows per digit, so we go 0..4
for row_idx in range(5):
    for digit_lines in patterns:
        # Print the row_idx-th line of this digit, plus two spaces as a separator
        print(digit_lines[row_idx], end="  ")
    print()
