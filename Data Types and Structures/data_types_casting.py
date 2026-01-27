# Casting (Type Conversion) in Python
#
# Casting means converting a value from one data type to another (e.g., from a string to an integer).
# Used when input data is in the wrong type for an operation (e.g., numbers entered as strings).
# Helps ensure variables have types appropriate for calculations, comparisons, or storage.
# Common Python casting functions include:
#
# int() – converts a value to an integer (if possible).
# float() – converts a value to a floating‑point number.
# str() – converts a value to a string.
# bool() – converts a value to a boolean.
#
#
# Casting may fail if the value isn’t compatible with the new type (e.g., int("hello") causes an error),
# so programs must handle such cases carefully.

age = input("What's your age?")
new_age = int(age) # This converts the input string into an integer. Without this, the program would crash.
if new_age >= 13:
    print("Ok, you can use this program.")
else:
    print("Sorry, too young. Go away.")