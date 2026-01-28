

#sequence - individual steps in a row, no changes possible
# print("Hello")
# print("My name is Mr. Computer.")
# print("My favourite number is 101001010010.")
# print("Ok bye.")


#binary selection
#a binary selection has only TWO possible options
# temperature = int(input("What is the temperature? "))
# if temperature > 30:
#     print("It's very hot!")
# else:
#     print("It's not very hot.")

#multiway selection
# age = int(input("How old are you? "))
# if age > 47:
#     print("You are old!")
# elif age > 17:
#     print("You are an adult.")
# else:
#     print("You are a child.")

#pre-test repetition
# counter = 0
#
# while counter < 5:
#     print("The counter value is:", counter)
#     counter += 1


# post-test repetition
# counter = 0

# while True:
#     print("The counter value is:", counter)
#     counter += 1
#
#     if counter >= 5:
#         break

#subprograms
#Subprograms, as the name implies, are complete part programs that are used from within the main program section.

# def average_numbers(x, y, z):
#     total = x + y + z
#     average = total / 3
#     return average
#
# def sum_numbers(x, y, z):
#     sum = x + y + z
#     return sum
#
# x = int(input("Type a number: "))
# y = int(input("Type a number: "))
# z = int(input("Type a number: "))
#
# print(f"The average is: {average_numbers(x, y, z)}.")
# print(f"The total is {sum_numbers(x, y, z)}.")

# total = 0
# def average(numbers_list):
#     for num in numbers_list:
#         total = total + num
#     average = total/len(numbers_list)
#     return average
#
# numbers = input("Type some numbers. As many as you like: ")
# numbers_list = numbers.split
# print(numbers_list)
#
# print(average(numbers_list))



#pre-test counted repetition
# for i in range(6):
#     value = int(input("Enter a value: "))
#     counter = i + 1
#
#     if value > counter:
#         print(value)
#     else:
#         print(counter)