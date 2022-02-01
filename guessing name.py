answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: #so it's greater
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You got it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it the first time")

if guess == answer:
    print("you got it the first time")
else:
    if guess > answer:
        print("guess lower")
    else:
        print("guess higher")
    guess = int(input())
    if guess == answer:
        print("You got it now")
    else:
        print("Sorry you have not guessed correctly")










# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guesses it")
#     else:
#         print("Sorry you didn't guess correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you didn't guess correctly")
# else:
#     print("You got it first time")
