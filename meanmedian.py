#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class

theList = []                                        #Empty list with empty square brakets.

for i in range(5):                                  #Repeat code 5 times
    theList.append(int(input(f"Number {i+1}:")))    #i+1 to get 12345 not 01234

print("as entered: " + str(theList))                #String function to print all values of theList

theList.sort()                                      #Sort the list, Default is Small to Large

print(f"small to large: {theList}")                 #String formatting to print the list

theList.sort(reverse=True)                          #To sort a list (in reverse) from Large to Small

print(f"large to small: {theList}")                 #String fomatting to print

median = theList[2]                                 #Just grabbing value out of list, no calc

sum = 0                                             #Initialize sum to zero

for i in range(5):        
    sum += theList[i]                               #Using i value as the index

mean = sum / 5

print (f"The median is {median} and the mean is {mean}")

