for i in range (1, 101): # loops through the numbers 1 to 100
    if i % 3 == 0 and i % 5 == 0: # checks if the number is divisible by both 3 and 5
        print ("FizzBuzz")
    elif i % 3 == 0: # checks if the number is divisible by 3
        print ("Fizz")
    elif i % 5 == 0: # checks if the number is divisible by 5
        print ("Buzz") 
    else: # if none of the above is true, print the number itself
        print (i)