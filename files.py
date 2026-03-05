fileName = 'demo.txt'
WRITE = 'w'
APPEND = 'a'

data = input('Please enter file info: ')

file = open(fileName, mode = WRITE)
file.write(data)
file.close()

#file = open(fileName, mode = WRITE)
#file.write('Susan, 29\n')
#file.write('Christopher, 31')
#file.close()

print('File demo.txt written successfully')

def writeText(data, filename):
    file = open(filename, mode = 'w')
    file.write(data)
    return

writeText('Hello, world.', 'c:\\users\\chharri\\documents\\hello.txt')

import csv

#Open my file
with open("demo.txt","r") as animalFile :
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList :
        print(';'.join(currentRow))


#for currentWord in currentRow :
        #    print(currentWord)



##Read file line by line
#firstAnimal = animalFile.readline()
#print(firstAnimal)
#secondAnimal = animalFile.readline()
#print(secondAnimal)

##read all file contents
#allFileContents = animalFile.read()
#print(allFileContents)

#Declare variables to hold the file name and access mode
fileName = "GuestList.txt"
accessMode = "w"

#Open the file for writing
myFile = open(fileName, accessMode)

#Write the guest names and ages to the file
for index in range(5) :
    name = input("Enter guest name: " )
    age = input("Enter guest age: " )
    myFile.write(name + "," + age  + "\n")

#Close the file
myFile.close()

print('File Guestlist.txt written successfully')

#import the csv library which contains functions to help you work with CSV files
import csv 

#Declare variables to hold the file name and access mode
fileName = "GuestList.txt"
accessMode = "r"

#open the file 
with open(fileName, accessMode) as myCSVFile:
    #Read the file contents 
    #specify that we are using a comma to separate the values in the file
    dataFromFile = csv.reader(myCSVFile, delimiter =",")

    #Create a for loop that will run once for each row in the list
    for row in dataFromFile :
        #print an entire row at a time in a list format
        print(row) 

        #print the entire row separating the values in the list with a comma
        print (', '.join(row))

        #Print each indivudal value in each row
        for value in row :
            print(value + "\n")

#Close the file
myCSVFile.close()

#Declare variables to hold the file name and access mode
fileName = "GuestList2.txt"
accessMode = "w"

#Open the file for writing
myFile = open(fileName, accessMode)

#Write the guest names and ages to the file

#I can write an entire record in one write statement
myFile.write("Doyle McCarty,27\n")
myFile.write("Jodi Mills,25\n")
myFile.write("Nicholas Rose,32\n")
#I could write the name and age in separate write statements
myFile.write("Kian Goddard")
myFile.write(",36\n")
myFile.write("Zuha Hanania")
myFile.write(",26\n")

#Close the file
myFile.close()

print('File Guestlist2.txt written successfully')

#import the csv library which contains functions to help you work with CSV files
import csv 

#Declare variables to hold the file name and access mode
fileName = "GuestList2.txt"
accessMode = "r"

#open the file 
with open(fileName, accessMode) as myCSVFile:
    #Read the file contents 
    #specify that we are using a comma to separate the values in the file
    dataFromFile = csv.reader(myCSVFile, delimiter =",")

    #Create a for loop that will run once for each row in the list
    for row in dataFromFile :
        #print an entire row at a time in a list format
        print(row) 

        #print the entire row separating the values in the list with a comma
        print (', '.join(row))

        #Print each indivudal value in each row
        for value in row :
            print(value + "\n")

#Close the file
myCSVFile.close()


#import libraries we will use
import sys

#Declare variables
filename = ""
fileContents = ""

#Ask the user for the filename
filename = input("PLease specify the name of the file to read ")

#open the file, since you may get an error when you attempt to open the file 
#For example the file specified may not exist
#put a try except statement around the command
try :   
    myFile = open(filename, "r")

    #I am using a boolean variable to determine if the file was found
    #That waythe code will only attempt to read the file if it was found succesfully
    fileFound = True

#Handle the FileNotFoundError
except FileNotFoundError :
    print("Could not locate file " + filename)
    fileFound = False

#Other errors could occur, perhaps the file is coorupte, or I do not have permissions on the file
except :
    error = sys.exc_info()
    print(error)
    fileFound = False

#if the file was opened successfully read the contents and display the contents to the user
if  fileFound :
    #Get the file contents into a string
    fileContents = myFile.read()
    print(fileContents)
#print the results 











