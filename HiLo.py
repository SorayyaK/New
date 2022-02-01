low = 1
high = 1000

print("Please think a number between {} and {}".format(low, high))
#input("Press Enter to start ")
guesses = 0
while low != high:
    #print("\tGuessing in the range of {} to {}".format(low, high))
    guesses = guesses + 1
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Should I guess higher or lower?\
 Enter h or l or c if my guess was incorrect"
                     .format(guess).casefold())
    if high_low == "h":
        low = guess + 1
        # guess higher. The lower end of the range becomes 1 greater than the guess

    elif high_low == "l":
        high = guess - 1
        # guess lower. The hight end of the range becomes one less than the guess.
    elif high_low == "c":
        print("I got it in {}".format(guesses))
        break
    else:
        print("Please enter, 'l', 'h', or 'c' ")

else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))

