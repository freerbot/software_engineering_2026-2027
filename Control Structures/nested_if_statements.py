raincheck = input("Is it raining?")
if raincheck == "yes":
    print("Take the MTR")
elif raincheck == "no":
    distance = int(input("How far is your destination"))
    if distance > 10:
        print("Take the MTR")
    elif 10 >= distance >= 2:
        print("Take a bike")
    elif distance < 2:
        print("Walk")






# food_pref = input("Are you allergic to foods?")
#
# if food_pref == "yes":
#     allergy = input("What are you allergic to?")
#     if allergy == "dairy":
#         print("Have some peanuts.")
#     elif allergy == "peanuts":
#         print("Have an apple.")
#     else:
#         print("Hmm, not sure what to tell you..")
# else:
#     print("Have some cheese and peanuts.")
#
# print("Bye!")