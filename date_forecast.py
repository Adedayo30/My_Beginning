#This program tells you future date when you enter the number of hours
from datetime import datetime, timedelta

print('This program tells you date interval from today.')
from_user = int(input('Enter numbers of hours you want to check: '))

today = datetime.now()
new_date = today + timedelta(hours=from_user)
print('Today\'s date is : ',today.strftime('%A %d %b, %Y'))
print('Next ', from_user,'hours will be: ', new_date.strftime('%A %d %b, %Y'))
