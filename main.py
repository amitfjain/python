from menu import MENU, resources

milkQt = 0
coffeeQt = 0
waterQt = 0
cost = 0.0

def coffeeRequirement(orderDrink):
    global milkQt
    global coffeeQt
    global waterQt
    global cost

    for eachDrink in MENU:
        # print(eachDrink)
        if eachDrink == orderDrink:
            for eachIngredient in MENU[eachDrink]:
                # print (MENU[eachDrink][eachIngredient])
                if eachIngredient == "cost":
                    cost = MENU[eachDrink][eachIngredient]
                    # print(f"{eachDrink} costs ${cost}")
                # elif eachIngredient == "ingredients":
                itemIngredients = MENU[eachDrink][eachIngredient]
                if eachIngredient == "ingredients":
                    for contents in itemIngredients:
                        if contents == "milk":
                            milkQt = itemIngredients[contents]
                        elif contents == "coffee":
                            coffeeQt = itemIngredients[contents]
                        else:
                            waterQt = itemIngredients[contents]

                        # print(f"{eachDrink} contains {contents} of {itemIngredients[contents]}")
                    # print(f"{eachDrink} contains milk: {milkQt}, coffee: {coffeeQt} & water: {waterQt}")
    # return cost, milkQt, coffeeQt, waterQt

def checkResources():
    print(milkQt, coffeeQt, waterQt)
    for eachItem in resources:
        if int(resources[eachItem]) > int(waterQt):
            if int(resources[eachItem]) > int(milkQt):
                if int(resources[eachItem]) > int(coffeeQt):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


user_choice = input("“What would you like? (espresso/latte/cappuccino): ").lower()
print(user_choice)
# print(coffeeRequirement(user_choice))
coffeeRequirement(user_choice)
if checkResources():
    print("Enough resources")
else:
    print("Insufficient resources")


