alien_color = input("Enter the colour of the alien:\n")
if alien_color == 'green':
    print("Player just earned five points.")
elif alien_color == 'yellow':
    print("Player just earned ten points.")
elif alien_color == 'red':
    print("Player just earned fifteen points.")

fav_fruits= ['apples', 'mangoes', 'oranges']
if 'bananas' in fav_fruits:
    print("You really like Bananas.")
if 'oranges' in fav_fruits:
    print("You really like oranges.")
if 'grapes' in fav_fruits:
    print("You reallyt like grapes.")

    prices = {
    "box_of_spaghetti" : 4,
    "lasagna" : 5,
    "hamburgers" : 2
}
quantity = {
    "box_of_spaghetti" : 6, 
    "lasagna" : 10,
    "hamburgers" :0
}
money_spent = 0


#for ott in prices:
 #   money_spent = money_spent + (prices[ott] * quantity[ott])
#print(money_spent)

#new_list_comprehension = [i+j for i in range(200) for j in range(50)]
#print(new_list_comprehension, end = " ")
x = "JOHN"
print(x.capitalize())
current_users = ['Admin', 'Njinwi', 'Jesse', 'Ngu-Ngwa', 'OTT', 'Prime']
new_users = ['Gregory', 'Bruno', 'Jesse', 'Christiano', 'Messi', 'Njinwi']
#user = input("Enter your username:\n")
for new in new_users:
    if new.capitalize() in current_users:
        print("That username is not available. Please enter another username.")
    else:
        print("That username is available.")
    
ordinal_nummbers= [1,2,3,4,5,6,7,8,9]
for number in ordinal_nummbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
