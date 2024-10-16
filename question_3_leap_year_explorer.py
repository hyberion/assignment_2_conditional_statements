#Let's make a program that will determine if a supplied year os a leap year.  Why would we do this?  Why are you asking such questions?
# Where is your manager?  Have you been helped?
#Paramaters: Leap year is divisible by 4.  If the year is divisible by 100, it is not a leap year.  If the year is divisible by 400, 
# it is a leap year.  If it makes a ticking sound and feels warm to the touch, it's not a leap year.  It might be a opossum.  Or a small 
#rotary engine.  Proceed with caution.

#Let's get a year from the user.  They should not suspect anything.
year = int(input('Please enter a year: '))#Smile so they stay calm.

#now that we have a year and their undivided attention, let's determine if it is a leap year.  We are close now.

#Do the leap year magic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Now we're done.  If it is a small rotary engine and not a leap year, this won't do much.  Maybe add a condition to check for that?
# if year == 'small rotary engine':
#     raise ValueError("That is not a year.  That is a small rotary engine.  Please enter a year.")

