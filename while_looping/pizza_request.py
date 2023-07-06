# The goal is for a user to input a topping, the topping is then added to a list
# and printed as a finished pizza

prompt = "\nPlease enter the pizza toppings you would like:"
prompt += "\nWhen finished, type 'finished' to order your pizza:"
prompt += "\nType 'quit' to quit the program:"

toppings= []

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    elif topping == 'finished':
        print(f"Your {toppings} pizza is finished!")
    else:
        toppings.append(topping)
        print(f"Adding {topping.title()}")
