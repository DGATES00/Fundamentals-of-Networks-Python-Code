# Author: Dykan Gates
# Please fill in the following functions below
# - DO NOT change the function definitions
# - This assignment will be graded with an automated grading script
# - Be sure that you have the correct 
# return type listed in the assignment

import math 
# For Problem One, I was tasked to write a function that reverse a string
def problem_one(test_string):
	original = ""
	for i in test_string:
		original = i + original
	return original

test_string = "Hello"
print("***Problem One***")  
print ("The original string  is : ",end="") 
print (test_string) 
  
print ("The reversed string is : ",end="") 
print (problem_one(test_string)) 
pass

# For Problem Two, I was taked to in a sentence return a list of all the words in that sentence
def problem_two(test_sentence):
	return (test_sentence[0].split())

print("\n***Problem Two***")
test_sentence = ["Hello World"]
print ("Original sentence was ", test_sentence)
print(problem_two(test_sentence))
pass

# For Problem Three, I was tasked to write a function that takes in a number and a list, and returns
# true if the number exists in the list
def problem_three(in_number,in_list):
# Checking if 1 exists in list  
	for i in in_list: 
		if(i == in_number):
			return print("It exists in this list")
		else:
			print ("false")

print("\n***Problem Three***")
in_list = [1, 2, 5, 6, 8, 9, 11]
in_number = 1
print("The list of numbers are " + str(in_list))
print("The number chosen is " + str(in_number))
print(problem_three(in_number, in_list))
pass

# For Problem Four, I was tasked write a function that takes in a number n and prints the sum of
# the numbers 1 to n.
def problem_four(in_number):
	sum = 0
	for i in range(0, in_number+1, 1):
		sum = sum+i
	return sum

print("\n***Problem Four***")
in_number = 5
print ("The number chosen is " + str(in_number))
print("The sum of the digits is " + str(problem_four(in_number)))
pass

# For Problem Five, I was tasked to write a function that concatenates two lists and removes duplicates
def problem_five(li_one, li_two):
	first_list = set(li_one)
	second_list = set(li_two)

	different_list = second_list - first_list
	result = li_one + list(different_list)
	print(result)

print("\n***Problem Five***")
li_one = [1, 4, 8, 9]
li_two = [2, 5, 7, 9]
print("First list: " + str(li_one))
print("Second list: " + str(li_two))
print(problem_five(li_one, li_two))
pass

# For Problem Six, I was tasked to write a function that takes in the radius of a circle compute the
# area of the circle.
def problem_six(radius):
	from math import pi
	print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))


print("\n***Problem Six***")
radius = float(input ("Input the radius of the circle : "))
print(problem_six(radius))
pass

# For Problem Seven, I was tasked to Write a function that creates a file with a speciic name(input),
# writes your name to the file, reads back from the file, then deletes
# the file. The function should return what is written in the file.
def problem_seven(file_name):
	import os

# Wrote my own name to file

	with open(file_name, 'w+') as f: f.write('Dylan Gates') 

# Read the file and stored my name

	with open(file_name, 'r+') as f: value = f.read()

# Delete the file

	os.remove(file_name)

# Return the value read from file

	return(value)

#print(create_read_del('myname.txt'))

print("\n***Problem Seven***")
file_name = "Problem.txt"
print(problem_seven(file_name))
pass

# For Problem Eight, I was tasked to write a function that counts the number of occurrence of a specific
# character in a string.
def problem_eight(test_string, test_char):
	# Count variable 
    result = 0
      
    for i in range(len(test_string)) : 
          
        # Checking character in string 
        if (test_string[i] == test_char): 
            result = result + 1
    return result 
print("\n***Problem Eight***")
test_string= "banana"
test_char = 'n'
print("Test word is: " + test_string)
print("Test character is: " + test_char)
print("There are " + str(problem_eight(test_string, test_char)) + " specific characters in this word")
pass

# For Problem Nine, I was tasked write a function to get the Python version you are using. 
def problem_nine():
	import sys
	print("Python version")
	print (sys.version)
	print("Version info.")
	print (sys.version_info)

print("\n***Problem Nine***")
print(problem_nine())
pass

#  For Problem Ten, I was tasked to write a function that will take in a list of email addresses and
#  return the domain and extension of each
def problem_ten(email_list):
	email_list = list()
	n = 6
	for i in range(0,n):
		info = input("email {}:\n".format(i))
		email_list.append(info) 

		domain = [i.split("@")[1] for i in emails] 
		res = list(dict.fromkeys(domain))
		return res
		result = domain_ext(n=4) 

print("\n***Problem Ten***")
email_list = ["testOne@gmail.com", "testTwo@gmail.com", "testThree@yahoo.com"]
print(problem_ten(email_list))
pass

# Put main here:
if __name__ == '__main__ ':
	print ( problem_one (test_string))
	print ( problem_two (test_sentence))
	print ( problem_three (in_number,in_list))
	print ( problem_four (in_number))
	print ( problem_five (li_one, li_two))
	print ( problem_six (radius))
	print ( problem_seven (file_name))
	print ( problem_eight (test_string, test_char))
	print ( problem_nine ())
	print ( problem_ten (email_list))

