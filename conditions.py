age = int(input("How old are you? "))
# if age >= 16 and age <=65:
if 16 <= age <= 65:
    print("Have a good day at work")

print("_" * 80)

if age < 16 or age >65:
    print("Enjoy your free time")

if age in range(16, 66):
    print("We can use 'in the range' like this")

