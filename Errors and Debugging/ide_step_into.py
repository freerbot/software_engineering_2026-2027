# This program can be used as an example of how the 'Step Into' feature of
# your IDE could be used.
#
# If you set a breakpoint on the line with
# order_total = process_order(100), it will first show the values of the
# variables and then when you use 'Step Over', it will move on to the next
# line of code print("We're finished..") and then end the program.
#
# If you use 'Step Into' instead, it will follow the flow of your code
# into the process_order() function. And if you continue using 'Step Into',
# it will also go into the apply_member_discount() function, which is inside
# the process_order() function. And if you continue further, it will move
# on to the apply_member_discount() function which is inside the
# apply_member_discount() function. This could be useful if you're trying to
# find a bug that's inside one of those functions. With 'Step Over', you bypass
# all of the code inside those functions.
#
# So whether you use 'Step Over' or 'Step Into' depends on what level of detail
# you want to look at during the debugging process.

def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

def apply_member_discount(price):
    member_discount = 15
    discounted_price = calculate_discount(price, member_discount)
    return discounted_price

def process_order(item_price):
    print(f"Original price: ${item_price}")
    final_price = apply_member_discount(item_price)
    print(f"Final price: ${final_price}")
    return final_price

# Main code
order_total = process_order(100) # try a breakpoint here
print("Ok, we're finished now..")
