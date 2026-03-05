guests = ['Susan','Christopher','Bill','Satya','Sonal']

print('print all 5 names:')
#option two for looping through a list
for currentGuest in guests :
    print(currentGuest)

##option one for looping through a list
#nbrValueInList = len(guests)
#for steps in range(nbrValueInList) :
#    print(guests[steps])


#remove a value from the list
guests.remove('Satya')
del guests[0]
print ('print 2nd name after deleting 1st name:')
print(guests[0])
print ('print last name:')
print (guests[-1])


##add a value
guests.append('Colin')
print('print last name after adding Colin')
print (guests[-1])

##update a value
print ('change 4th name to Sonia')
guests[3] = 'Sonia'
print (guests[3])

