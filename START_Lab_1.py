def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it

    # convert from gb to mb to kb to b
    num_bytes = input_gb * 1024 * 1024 *1024

    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    # not a string
    if type(name) != type(str):
        return None
    # continute
    length = len(name)
    if length % 2 == 0:
        # no remainder = even
        is_odd = False
    elif length % 2 != 0:
        # remainder = odd
        is_odd = True
    else:
        print("Error")

    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    length = len(input_string)
    if input_number + 1 <= length:
        character_at = input_string[input_number]
    elif input_number + 1 > length:
        character_at = -1
    else:
        print("Oh no")

    return character_at


def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    file = open(file_name, "r")
    # numbers are sorted line by line, thus read lines
    # this parses the file into a list line by line, which is how our file is organized
    # note: retains \n
    lines = file.readlines()
    # print(lines)
    for line in lines:
        # print(line)
        # nums to convert from string to int
        # this removes the \n
        list_of_nums.append(int(line))

    return list_of_nums

# # test 1
# file_name = "github/test_file1.txt"
# print(lab1Question4(file_name))

# # test 2
# file_name = "github/test_file2.txt"
# print(lab1Question4(file_name))



def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 

    # mode = the item that occurs the most in that list
    mode_of_list = None
    uniqueNums = []
    countNum = 0
    tempNum = 0
    # executes = 0

    # obtain all unique numbers
    for num in list_numbers:
        if num not in uniqueNums:
            uniqueNums.append(num)
    
    # list.count(item) gives the occurrence of the item in that list
    # count each unique number, and make that the mode if its the largest
    for uNum in uniqueNums:
        # executes += 1
        # print("Execute: ", executes)
        if mode_of_list == None:
            # first number check
            countNum = list_numbers.count(uNum)
            mode_of_list = uNum
        elif mode_of_list != None:
            # other numbers in list
            tempNum = list_numbers.count(uNum)
            if tempNum > countNum:
                # found higher occurrence of number, assign new count and mode
                countNum = tempNum
                mode_of_list = uNum
            elif tempNum == countNum:
                # count same, get the mode of the larger number mathematically
                if uNum > mode_of_list:
                    mode_of_list = uNum
        else:
            print("Oh no :(")
        # print(mode_of_list)

    return mode_of_list

# # Test case 1
# list_numbers = [1, 2, 3, 4, 5, 1]
# assert lab1Question5(list_numbers) == 1

# # Test case 2
# list_numbers = [10, 20, 30, 40, 50, 10, 20, 20]
# assert lab1Question5(list_numbers) == 20

# # Test case 3
# list_numbers = [1, 1, 2, 2, 3, 3, 3]
# assert lab1Question5(list_numbers) == 3

# # Test case 4
# list_numbers = [100, 200, 300, 400, 500, 400]
# assert lab1Question5(list_numbers) == 400

# # Test case 5
# list_numbers = [1, 1, 1, 1, 1]
# assert lab1Question5(list_numbers) == 1


def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    quarter_total = quarters * 0.25
    # print(quarter_total)
    dime_total = dimes * 0.10
    # print(dime_total)
    nickel_total = nickels * 0.05
    # print(nickel_total)
    penny_total = pennies * 0.01
    # print(penny_total)
    total = quarter_total + dime_total + nickel_total + penny_total

    return total

# # test 3 for Q6
# quarters = 10
# dimes = 5
# nickels = 2
# pennies = 1
# total = lab1Question6(quarters, dimes, nickels, pennies)
# print(total)

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.