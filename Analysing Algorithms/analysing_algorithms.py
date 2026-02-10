# 1. Identify Inputs and Outputs
# a) Inputs
#
# List every piece of data that the program receives from the user.
# Identify which function each input is used in.
# Write the data type of each input after type‑casting (e.g. integer, float, string).
#
# b) Outputs
#
# List every message or value the program displays to the user.
# Identify which function produces each output.


# 2. Determine the Purpose of the Algorithm
# For this section, write short, clear statements.
# a) Purpose of the overall program
# Explain in one or two sentences what the entire program is designed to do.
# b) Purpose of each subroutine (function)
# For each function:
#
# Write the function name.
# Explain what the function does.
# Describe the data it receives (parameters).
# Describe the data it returns (outputs).
#
# Functions to analyse:
#
# get_prices()
# calculate_total()
# apply_discount()
# choose_bonus_item()
# main()


# 3. Draw a Context Diagram for this program.

# 4. Draw a Data Flow Diagram for this program.

# 5. Write a data dictionary for this program.




import random

def get_prices(number_of_items):
    prices = []
    count = 0
    while count < number_of_items:
        price_text = input("Enter price for item " + str(count + 1) + ": ")
        price = float(price_text)
        if price > 0:
            prices.append(price)
            count = count + 1
        else:
            print("Price must be greater than 0.")
    return prices

def calculate_total(prices_list):
    total = 0
    for price in prices_list:
        total = total + price
    return total

def apply_discount(total_amount):
    if total_amount >= 100:
        discount_rate = 0.2
    elif total_amount >= 50:
        discount_rate = 0.1
    else:
        discount_rate = 0.0

    final_amount = total_amount - (total_amount * discount_rate)
    return final_amount, discount_rate

def choose_bonus_item():
    bonus_items = ["pen", "sticker", "bookmark", "keyring"]
    index = random.randint(0, len(bonus_items) - 1)
    return bonus_items[index]

def main():
    print("=== Simple Shop Checkout ===")

    items_text = input("How many items are you buying? ")
    number_of_items = int(items_text)

    prices = get_prices(number_of_items)

    total_before_discount = calculate_total(prices)

    final_total, discount_used = apply_discount(total_before_discount)

    print("Total before discount:", total_before_discount)
    print("Discount rate used:", discount_used)

    if final_total > 0:
        bonus = choose_bonus_item()
        print("You receive a bonus:", bonus)

    print("Final total to pay:", final_total)

main()