
#1. Python Program to remove duplicate characters from a String

def remove_duplicates(input_string):
    unique_chars = set()
    result_string = ""
    for char in input_string:
        if char not in unique_chars:
            unique_chars.add(char)
            result_string += char
    return result_string

string = "Hello Python"
result = remove_duplicates(string)
print("String without duplicates:", result)

#2. Python program to drop all digits from a String

def dropNumber(str_numbers):
    result = ""
    for str in str_numbers:
        if str.isalpha() or str.isspace():
            result += str
    return result

mystr = "He12llo, Py00th55on!"
final_result = dropNumber(mystr)
print("The String without number is : " , final_result)

#3. Print the Following pattern,using loop.
#
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

row = 6
for i in range(row):
    for j in range(i):
        print(i, end=" ")
    print('')

#4. Python program to list unique characters with their with their count in a String (3 Mark)
#Input: str = "madam"
#Output: 3
def count_Char(str_string):
    char_count= set(str_string)
    count_chars = len(char_count)
    
    return count_chars


str_string = input("Please enter a word: " )
Output = count_Char(str_string)
print("Number of Unique character is: ", Output)


#5 Check if the first and last number of a list is the same, Write a function to return True if the first 
# and last number of a given list is same. If numbers are different then return False

def Check_Equality(number):
    if len(number) >= 2:
        return number[0] == number[-1]
    else:
        return False
    
numbers_x = [11, 20, 30, 40, 11]
numbers_y = [25, 65, 35, 75, 30]

equality_x = Check_Equality(numbers_x)
equality_y = Check_Equality(numbers_y)

print(f"The result of list number x is:  {equality_x}")
print(f"The result of list number y is: {equality_y}")


#6: Write a program to check if the given number is a palindrome number. A palindrome number is a number 
# that is the same after reverse. For example,242, is the palindrome numbers (1 Mark)

def is_Palindrom(number):
    number_str = str(number)
    return number_str == number_str[:: -1]

number = 242
result2 = is_Palindrom(number)
if result2:
    print("This number is a Palindrom: " , number)
else: 
    print("It's not a palindrom" , number)
    
#7: Create a new list from two list using the following condition:Given two list of numbers, write a 
# program to create a new list such that the new list should contain odd numbers from the first list and 
# even numbers from the second list
def new_List(list1, list2):
    result_list = []
    result_list.extend([num for num in list1 if num % 2 != 0])
    result_list.extend([num for num in list2 if num % 2 == 0])
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
final_list = new_List(list1,list2)
print(f"The new list is: {final_list}" )
