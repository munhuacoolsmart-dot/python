import datetime

currentDate = datetime.datetime.today()
#print(currentDate)
#print(currentDate.minute)
#print(currentDate.month)
#print(currentDate.year)

#print(currentDate.strftime('%d %b, %Y'))
print(currentDate.strftime('%d %b %y'))


userInput = input('Please enter your birthday (dd/mm/yyyy) ')
birthday = datetime.datetime.strptime(userInput,'%d/%m/%Y')

#print(birthday)

days = birthday - currentDate
years= abs( round(days.days/365,0))
print("You are "+str(years)+" years old.")