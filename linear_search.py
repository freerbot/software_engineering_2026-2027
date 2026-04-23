array = [1,8,3,33,15,20,10]
print(f"This is the array: {array}")
target = int(input("Number to search for: "))
found = False

for i in range(0, len(array)):
    if array[i] == target:
        print(f"found {target} at index {i}")
        found = True
        break

if found == False:
    print("not found")


# BEGIN linear search
# set target to the number you're searching for
# set array to contents of array
# set found to False
#
# FOR i = 0 to length of array
#    IF index i is target
#       print "target found at index"
#       set found to True
#       exit loop
# NEXT i
#
# IF found is False THEN
#   print "target not found"
#
# END linear search




# def search(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#
#     return("not found")
#
#
# print(search(array,target))









# print("finished searching")


# def search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#
#     return("not found")
#
# print(search(array,102))



# for each element in the array, check if it is equal to our target.
# if the element is equal to our target, tell the user 'yes' and which element it is
# if the element is not equal to target, move to the next element
# if you get to the end and none of the elements are equal to target, tell user 'no'




# for i in range(len(array)):
#     print(i)
#
# #Linear Search
















# def search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#
#     return("not found")
#
# print(search(array,102))