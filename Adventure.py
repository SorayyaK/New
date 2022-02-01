available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction : ")
    if chosen_exit.casefold() == "quit":
        print("Game's over")
        break
else:
    print("aren't you glad you got out of there?")


# for i in range(0, 10):
#     print(i)
#     if i > 0 and i % 5 == 0:
#         break
