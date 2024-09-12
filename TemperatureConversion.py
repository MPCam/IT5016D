#TemperatureConversion.py
#M.Campbell
#28/08/2024

temperature = input('Please enter fahrenheit or celsius\n')
print('You inputted ',temperature)

# calculation and display depending on user input
if temperature == 'fahrenheit':
    number = int(input('Please enter number to convert\n'))
    print('You inputted ', number)
    print(number, 'is', number*9//5+32, 'in fahrenheit')
elif temperature == 'celsius':
    number = int(input('Please enter number to convert\n'))
    print('You inputted ', number)
    print(number, 'is', (number-32)*5//9, 'in celsius')
else:
    print('Only put fahrenheit or celsius')
