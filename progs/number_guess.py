secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
muggles_number = int(input())

while muggles_number != secret_number:
    print(
        """
+================================+
| MUAHAHAAHAHAHA You suck!       |
| You would never be chosen      |
| to be in the greatest house    |
| at Hogwarts School of          |
| of Witchcraft and Wizardy,     |
| Ravenclaw! Now you are stuck   |
| in my loop until you guess     |
| the most magical number ever!  |
+================================+
""")
    muggles_number = int(input())

print(
"""
+================================+
| You guessed lucky you filthy   |
| Mudblood! My Father will hear  |
| about this!!!!                 |
+================================+
""")