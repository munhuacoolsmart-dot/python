#Declare and initialize the variables
monthlyPayment = 0
loanAmount = 0
interestRate = 0
numberOfPayments = 0
loanDurationInYears = 0

#Ask the user for the values needed to calculate the monthly payments
strLoanAmount = input("How much money will you borrow? ")
strInterestRate = input("What is the interest rate on the loan (/100)? ")
strLoanDurationInYears = input("How many years will it take you to pay off the loan? " )

#Convert the strings into floating numbers so we can use them in teh formula
loanDurationInYears = float(strLoanDurationInYears)
loanAmount = float(strLoanAmount)
interestRate = float(strInterestRate)

#Since payments are once per month, number of payments is number of years for the loan * 12
numberOfPayments = loanDurationInYears*12

#Calculate the monthly payment based on the formula
monthlyPayment = loanAmount * interestRate * (1+ interestRate) * numberOfPayments \
    / ((1 + interestRate) * numberOfPayments -1)

#provide the result to the user
print("Your monthly payment will be " + str(monthlyPayment))
print("Your monthly payment will be $%.2f" % monthlyPayment) 


#Extra credit
#meanwhile earlier in the day
bestTeam = "senators"

#if statements with strings
#favouriteTeam = input("What is your favourite hockey team? ")
#if favouriteTeam.upper() == bestTeam.upper() :
#    print("Yeah Go Sens Go")
#    print("But I miss Alfredsson")
#print ("It's okay if you prefer football/soccer")

#if with numbers
freeToaster = None 

deposit = int(input("how much do you want to deposit "))
if deposit > 100 :
    freeToaster = True

#complex code here...
if freeToaster :
    print("enjoy your toaster")
print("Have a nice day!")
