# #2
# def sayHello():
#     name = input('Enter your name: ')
#     print(f'Hello {name}')

# sayHello()

#3
# def calculatePay():
#     hours_worked = int(input('Enter hours worked: '))
#     hourly_rate = float(input('Enter hourly pay: '))
#     calculate_pay = hours_worked * hourly_rate
#     print(f'Pay: ${calculate_pay}')

# calculatePay()

#4
# width = 17
# height = 12.0
#
# print(type(width//2))
# print(type(width/2))
# print(type(height/3))

#5
# def celsius_to_fahrenheit():
#     celsius = float(input('Enter temperature in celsius: '))
#     fahrenheit = 1.8 * celsius + 32
#     print(f'{celsius}C is equal to {fahrenheit}F')
#
# celsius_to_fahrenheit()

#6
hours_worked = int(input('Enter hours worked: '))
hourly_rate = float(input('Enter hourly pay: '))
if hours_worked > 40:
    calculate_pay = (hours_worked - 40)*hourly_rate*1.5 + 40*hourly_rate
else:
    calculate_pay = hours_worked * hourly_rate

print(calculate_pay)