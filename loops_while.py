






# correct_username = "derp"
# correct_password = "derp1234"
# attempts = 0
# maximum_attempts = 3
# too_many_attempts = False
# username = ""
# password = ""
#
# while username != correct_username or password != correct_password:
#     if attempts == maximum_attempts:
#         too_many_attempts = True
#         break
#     print("\nPlease log in with \nyour username and password:")
#     username = input("Username: ")
#     password = input("Password: ")
#     attempts += 1
#
#
# if too_many_attempts == True:
#     print("The internet police have been called. You're going to jail, buddy.")
# else:
#     print("Log in successful.")


CORRECT_USERNAME = "derp"
CORRECT_PASSWORD = "derp1234"
MAXIMUM_ATTEMPTS = 3

attempts = 0
while attempts < MAXIMUM_ATTEMPTS:
    print("\nPlease log in with your username and password:")
    username = input("Username: ")
    password = input("Password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Log in successful.")
        break

    attempts += 1

if attempts == MAXIMUM_ATTEMPTS:
    print("The internet police have been called. You're going to jail, buddy.")





# correct_username = "derp"
# correct_password = "derp1234"
#
# username = ""
# password = ""
# tries = 0
#
# while username != correct_username or password != correct_password:
#     print("\nPlease log in with your username and password:")
#     username = input("Username: ")
#     password = input("Password: ")
#
# print("Log in successful.")