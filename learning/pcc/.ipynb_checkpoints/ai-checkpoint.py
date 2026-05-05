mbappe = {
    "first_name" : 'kylian',
    "last_name" : 'mbappe',
    "city" : 'madrid',
    "age" : 27,
    }
print(mbappe)
fav_numbers = {
    "james" : 57,
    "chris" : 67,
    "jessica" : 78,
}
best_friends = ['jessica', 'chris']

for name, number in fav_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")
    print(f"Hi {name.title()}.")

    if name in best_friends:
        language = fav_numbers[name]
        print(f"\t{name.title()}, I see you love {language}!")
print(fav_numbers)


terms = {
    "dictionary" : 'saved with braces',
    "list" : 'saved with square brackets',
    "tuples" : 'saved with parantheses'
}
for key, value in terms.items():
    print(f"A {key} is saved with {value}")