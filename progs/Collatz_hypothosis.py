while True:
    try:
        c0 = int(input("Input a natural number: "))
        if c0 == 0:
            error = "The number cannot be 0."
            raise ValueError("The number cannot be 0.")
        if c0 == 1:
            error = "The number cannot be 1."
            raise ValueError("The number cannot be 1.")
        if c0 < 1:
            error = "The number must be positive."
            raise ValueError("The Number is not positive.")
        break
    except ValueError:
        print(error + " Please enter a positive integer.")
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        #even
        c0 = c0 // 2
    else:
        #odd
        c0 = 3 * c0 + 1
    print(c0)
    steps += 116
    
print("Steps: " + str(steps))
input_ratio = c0 / steps
print("Input Ratio: " + str(input_ratio))