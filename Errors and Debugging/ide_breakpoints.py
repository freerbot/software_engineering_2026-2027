def calculate_total(prices):
    total = 0
    for price in prices:
        total = total + price # try a breakpoint here
    return total

shopping_cart = [10, 25, 5, 30]
result = calculate_total(shopping_cart)
print(f"Total: ${result}")

