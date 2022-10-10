#Program in Python to count the occurences of a character in user input string

string = input("Please enter  String : ") #user input string
char = input("Please enter a Character of your choice : ") #user input character

count = 0
for i in range(len(string)): #for loop to iterate over
    if(string[i] == char):
        count = count + 1

print("The total Number of Times ", char, " has Occurred = " , count) #print statement to show result