#paste code here
import time #So that the table doesn't all print at once

number = "" # The first assignment of the num

def times(number): #Make it a function that you can repeat if required
#Ask the user to choose a times table
    number = input("What times table do you want me to display? >>> ")
#Check the user has entered something sensible
    if number != int(): #For some reason this isn't working... tried everything
        print("I don't understand.")
        times(number)
    elif number > 101:
        print("That number is too high!")
        times(number)
    elif number < -11:
        print("That number is too low!")
        times(number)
    else:
#Display the times table for that number up to 12x
        for x in range(0,13):
            print(x, "x", number, "=", (number*x))
            time.sleep(0.5)
            x = x+1

#Run the program
times(number)
