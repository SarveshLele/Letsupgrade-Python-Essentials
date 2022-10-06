#Getting number from user   
num = int(input("Enter a number to check even or odd"))

if num%2 == 0:      #Checking if number is even
    print("Number is Even!")
elif num%2 == 1:    #Checking if number is odd
    print("Number is Odd!")
else:               #If number is 0
    print("Number is 0!")
