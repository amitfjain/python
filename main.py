from menu import MENU, resources
from art import logo

isMachineON= True
milkQt = 0
coffeeQt = 0
waterQt = 0
cost = 0.0
cashBox = 0.0

def printReport():
    global cashBox
    for eachIngredient in resources:
        print(f"{eachIngredient}: {resources[eachIngredient]}")
    print(f"Money: {cashBox}")

def coffeeRequirement(orderDrink):
    global milkQt
    global coffeeQt
    global waterQt
    global cost

    # if orderDrink == "report":
    #     printReport()
    # else:
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
    # print(milkQt, coffeeQt, waterQt)
    for eachItem in resources:
        # print(eachItem: resources[eachItem])
        if eachItem == "water":
            if (int(resources[eachItem]) >= int(waterQt)):
                return True
            else:
                print("Sorry there is not enough water")
                return False

        if eachItem == "milk":
            if (int(resources[eachItem]) >= int(milkQt)):
                return True
            else:
                print("Sorry there is not enough milk")
                return False

        if eachItem == "coffee":
                if (int(resources[eachItem]) >= int(coffeeQt)):
                    return True
                else:
                    print("Sorry there is not enough coffee")
                    return False



def cashier():
    print = "Please insert coins. "
    quarters = int(input("How many quarters? ")) * .25
    dimes = int(input("How many dimes? ")) * .1
    nickels = int(input("How many nickels? ")) * .05
    pennies = int(input("How many pennies? ")) * .01
    total = quarters + dimes + nickels + pennies
    return total

def updateResources():
    for eachIngredient in resources:
        if eachIngredient == "coffee":
            if int(resources[eachIngredient]) > 0:
                resources[eachIngredient] -= coffeeQt

        if eachIngredient == "water":
            if int(resources[eachIngredient]) > 0:
                resources[eachIngredient] -= waterQt

        if eachIngredient == "milk":
            if int(resources[eachIngredient]) > 0:
                resources[eachIngredient] -= milkQt






# print(user_choice)
# print(coffeeRequirement(user_choice))
print (logo)
while isMachineON:
    user_choice = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        printReport()
    else:
        coffeeRequirement(user_choice)
        if checkResources():
            # print("Enough resources")
            userBalance = cashier()
            if cost > userBalance:
                print("Sorry there is not enough money. Money refunded.")
            else:
                updateResources()
                userBalance -= cost
                cashBox += cost
                print(f"Here is $ {userBalance} in change")
                print(f"Here is your {user_choice} ☕️ Enjoy!")







