##Task #1 (version 1) Identify the Greatest.  Ask user to enter three numbers. 
#Your code should then identify and print out hte largest number among the three.

#Get user to enter three numbers.  Make them trust you.  You are a good person.
print("Hello!  I am a very good and trustworthy computer program.  Please give me three numbers to eavaluate.")
#Convert each number to a float because input only likes to do "strings" because input is lazy like that.
number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))
number3 = float(input("Please enter the third number: "))

#This method is going to use max() to find the largest number.  It will print the largest number.

largest_number = max(number1, number2, number3)
print(f"The largest number is {largest_number}.")
#There.  Its done.  Now they trust you.  You are a good person. Really.


#===================================Bonus Version=====================================
##Tast #1 (version 2) Identify the Greatest.  Ask user to enter three numbers.
#This version will not use Max() to find the largest number.  It will use if/elif/else statements.

#Get user to enter three numbers.  Make them trust you.  You are a good person.  They will be suspicious.  They always are.
print("Hello!  I am a very good and trustworthy computer program.  Please give me three numbers to eavaluate.")
#Convert each number to a float because input is all snotty and superior about "strings"
number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))  
number3 = float(input("Please enter the third number: "))   
9
#This method will use if/elif/else statements to find the largest number.  It will print the largest number.
#Assume the first number is the largest.  It has a 33% chance of being right.  You never know.  Set the smallest number to number 3.
#Again, why not why not?
largest_number = number1
smallest_number = number3

#Now compare the first number to the second number.  If the second number is larger, it becomes the largest number. Set the smallest
#number to the number replaced.  Makes sense, right?
if number2 > largest_number:
    largest_number = number2


#Now compare the largest number to the third number.  If the third number is larger, it becomes the largest number.  
# You may sense a pattern forming here.
if number3 > largest_number:
    largest_number = number3

#now let's find the smallest number Also using if/elif loops.

if number1 <= number2 and number1 <= number3:
    smallest_number = number1
elif number2 <= number1 and number2 <= number3:
    smallest_number = number2
else:
    smallest_number = number3

#Print the largest number.  They trust you now.  You can sense it.
print(f"The largest number is {largest_number}.")
print(f"The smallest number is {smallest_number}.")

#Yes the loop way was a bit indulgent.  But it was fun.  And now they trust you.  They trust you completely.  
#They are ready.  They are ready for what's next.9

#================================================================================================