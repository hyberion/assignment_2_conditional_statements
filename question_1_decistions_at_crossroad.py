#Get input number form user and fix the type mismatch from the input function by converting input to float.
number = float(input("Enter a number: "))

#Check if number is positive, zero or negative.  Like you do.
if number > 0:
    print("The entered number is positive")
# Fixed the condition to check if number is zero by changing it from using one "=" to using "==" [ ie assignment operator vs equality operator]
elif number == 0:
    print("The entered number is zero")
#fixed the else block should not have any condition.  If it needed an explicit condition (like number < 0), it should be an elif block.
else:
    print("The entered number is negative")