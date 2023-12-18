# # The user enters a collection of numbers (using input) and lists all numbers greater than the 3rd smallest number

# x = int(input("Enter the 1. number:"))
# y = int(input("Enter the 2. number:"))
# z = int(input("Enter the 3. number:"))

# list = [x , y, z]
# max = list[0]
# for f in list: 
#     if(f<max):
#         max = f
# print(max)
# print(list)


def remove_repeating_same_letter(string):
    new_string = ""
    prev_letter = ""
    for letter in string:
        if letter != prev_letter:
            new_string += letter
            prev_letter = letter
    return new_string

print(remove_repeating_same_letter("aaahhhojjj    jaaaaak seeee maaaas"))



