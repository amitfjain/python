from menu import resources, MENU

# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

user_choice = input("“What would you like? (espresso/latte/cappuccino): ")

# TODO Turn off the Coffee Machine by entering “off” to the prompt.


# TODO Print report.
for eachItem in resources:
    print(f"{eachItem}: {resources[eachItem]}")


# TODO Check resources sufficient?
def check_requirement(ordered_drink):
    drink_details_dictionary = {}
    water = ""
    coffee= ""
    milk = ""

    for eachItem in MENU:
        if eachItem == "espresso":
            drink_details_dictionary = ordered_drink[0][0]
            for eachIngredient in drink_details_dictionary:
                print (eachIngredient)
                if eachIngredient == "water":
                    water = drink_details_dictionary[eachIngredient]
                elif eachIngredient == "coffee":
                    coffee = drink_details_dictionary[eachIngredient]
                elif eachIngredient == "milk":
                    milk = drink_details_dictionary[eachIngredient]


        elif eachItem == "latte":
            drink_details_dictionary = ordered_drink[1][0]
            for eachIngredient in drink_details_dictionary:
                print(eachIngredient)
                if eachIngredient == "water":
                    water = drink_details_dictionary[eachIngredient]
                elif eachIngredient == "coffee":
                    coffee = drink_details_dictionary[eachIngredient]
                elif eachIngredient == "milk":
                    milk = drink_details_dictionary[eachIngredient]

        elif eachItem == "cappuccino":
            drink_details_dictionary = ordered_drink[2][0]
            for eachIngredient in drink_details_dictionary:
                print(eachIngredient)
                if eachIngredient == "water":
                    water = drink_details_dictionary[eachIngredient]
                elif eachIngredient == "coffee":
                    coffee = drink_details_dictionary[eachIngredient]
                elif eachIngredient == "milk":
                    milk = drink_details_dictionary[eachIngredient]

    print(f"Water: {water}, Milk: {milk}, Coffee: {coffee}")

                # print(eachIngredient)
check_requirement(user_choice)
# TODO  Process coins.

# TODO Check transaction successful?

# TODO Make Coffee.
