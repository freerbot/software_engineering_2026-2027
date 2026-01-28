#The print() function is used to output to your console.
#This is useful for writing text-based programs where the user must
#interact with the program by reading/typing text.
#It's also useful for debugging your code. For example, printing the
#value of a variable to find out why your program is behaving a certain way.

print("Hello")  # prints the word Hello as a string
print(5) # prints the number 5 as an integer

dog_name = "Kenny"
print("You can combine strings like this. One of my dogs is named " + dog_name + ".")
print(f"You can also combine strings like this. One of my dogs is named {dog_name}.")
# By adding that f at the start of the function, you can insert variables by using {variable_name}.
# This makes your code look a bit less confusing.