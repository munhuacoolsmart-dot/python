#import turtle

#counter = 0
#while counter < 4:
#    turtle.forward(100)
#    turtle.right(90)
#    counter += 1 # This is the exact same thing as counter = counter + 1




#nested while
i =7
while i > 0:
    j = 0
    while j < i:
        print("#", end="")
        j += 1
    print()
    i -= 1
    
    
    
#nested do while loop
i = 1
while True:
    j = 0
    while j <= i-1:
        print("#", end="")
        j += 1
    print()
    i += 1
    if i ==8:
        break

#nested for and while loops

rows =7

for i in range(rows, 0, -1):   # controls rows
    
    # spaces using while
    space = 0
    while space < (rows - i):
        print(" ", end="")
        space += 1
    
    # hashes using while
    hash = 0
    while hash < i:
        print("#", end="")
        hash += 1
    
    print()
    
    
#nested for loop
for i in range(1,8):
    # Print spaces
    for space in range(7 - i):
        print(" ", end="")
    
    # Print hashes
    for hash in range(i):
        print("#", end="")
    
    print()
    
    
#while and do while loop
rows =4
i = rows   # start from 3 and go down

while i > 0:   # WHILE loop controls rows
    
    # DO-WHILE style for spaces
    space = 0
    while True:
        if space >= (rows - i):
            break
        print(" ", end="")
        space += 1
    
    # DO-WHILE style for hashes
    hash = 0
    while True:
        if hash >= (2 * i - 1):
            break
        print("#", end="")
        hash += 1
    
    print()
    i -= 1

#for and do while loop
rows=4

for i in range(1, rows + 1):   # FOR loop controls rows
    
    # DO-WHILE style for spaces
    space = 0
    while True:
        if space >= (rows - i):
            break
        print(" ", end="")
        space += 1
    
    # DO-WHILE style for hashes
    hash = 0
    while True:
        if hash >= (2 * i - 1):
            break
        print("#", end="")
        hash += 1
    
    print()
