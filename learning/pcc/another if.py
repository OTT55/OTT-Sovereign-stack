test = (input("Enter your name:"))
name = ['Rudiger', 'Yoro', 'Maguire', 'Araujo', 'Courtois', 'Lemmens', 'Donnaruma','Bruno Fernandes', 'Mainoo', 'Bellingham', 'Pedri','Mbappe', 'Haaland', 'Mbeumo', 'Sesko']
if test.capitalize() in name:
   print(f"You are a great player {test.capitalize()}")
else:
   print(f"You are not a great according to our data, {test.capitalize()}")


ages = [12, 18, 25, 30, 40, 33, 67]
weights = [50, 60, 70, 80, 90, 100, 110]
heights = [150, 160, 170, 180, 190, 200, 210]
number = int(input("Enter a number: "))
for age in ages: 
    if number == age and number in ages:
        print(f"{number} is in the ages list.")
    elif number > age and number in ages:
        print(f"{number} is greater than {age} in the ages list but is in the ages list.")
    elif number < age and number in ages:
        print(f"{number} is less than {age} in the ages list but is in the ages list.")
    else:
        print(f"{number} is not in the ages list.")
for weight in weights: 
    if number == weight and number in weights:
        print(f"{number} is in the weights list.")
    elif number > weight and number in weights:
        print(f"{number} is greater than {weight} in the weights list but is in the weights list.")
    elif number < weight and number in weights:
        print(f"{number} is less than {weight} in the weights list but is in the weights list.")
    else:
        print(f"{number} is not in the weights list.")
