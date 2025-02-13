# text = 'hello world'
# print(text.split())
import random

while True:
    name = input("Please enter your full name: ")
    split_name = name.split()
    if len(split_name) >= 2:
        break
    print("Please enter both your first and last name.")

first_name = split_name[0].lower()
last_name = split_name[1].lower()

combo1 = first_name + last_name
combo2 = last_name + last_name
combo3 = first_name[:4] + last_name[-3:]
combo4 = last_name[-2:] + first_name[-1:]
number = random.randint(0, 100)
combo5 = first_name + str(number)
combo6 = last_name + str(number)

name_combos = [combo1, combo2, combo3, combo4, combo5, combo6]

random_name = random.choice(name_combos)
print("Generated Name:", random_name)




