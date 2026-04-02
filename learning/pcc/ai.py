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


for ott in prices:
    money_spent = money_spent + (prices[ott] * quantity[ott])
print(money_spent)

new_list_comprehension = [i+j for i in range(200) for j in range(50)]
print(new_list_comprehension, end = " ")