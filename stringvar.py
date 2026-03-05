#initialize the variables
girldescription = " " 
boydescription = " " 
walkdescription = " " 
girlname = " "
boyname = " "
animal = " "
gift = " " 
answer = " "

#Collect name from the user
name = input('What is your name? ')
country = input('What country do you live in? ')
country = country.upper()

#Display the name
#print(name)

#Ask the user to specify values for the variables
girlname = input("Enter a girl's name: ")
boyname = input("Enter a boy's name: " )
animal = input("Name a type of animal you ride on: " )
gift = input("Name something you give to a girl: ")
girldescription = input("Enter a description of the girl:")
boydescription = input("Enter a description of the boy: ")
walkdescription = input("Enter a description of how the girl might walk: " )
answer = input("What would you say to someone who gave you a gift: ")

#Create a friendly output
print('\nHello, ' + name + '. You live in ' + country)

#Update the value
#name = 'Christopher Harrison'
#print(name)

#Display the story
#Don't forget to format the strings when they are displayed
print ("Once upon a time,")
print("there was a girl named " + girlname.capitalize() + ".")
print("One day, " + girlname.capitalize() + " was walking " + walkdescription.lower() + " down the street.")
print("Then she met a " + boydescription.lower() + " boy named " + boyname.capitalize() + " who gave her a "+gift.lower()+".")
print("He said, 'You are really " + girldescription.lower() + "!'")
print("She said '" + answer.capitalize() + ", " + boyname.capitalize() + ".'")
print("Then they both rode away on a " + animal.lower() + " and lived happily ever after.")




