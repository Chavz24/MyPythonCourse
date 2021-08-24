"""Challenge: Convert Temperatures 6.3"""


# Write a script called temperature.py that defines two functions:
# convert_cel_to_far() and convert_far_to_cel().

def convert_cel_to_far(celsius):
    """This function takes degrees Celsius and convert them to Fahrenheit"""

    f = ((celsius * 9) / 5) + 32
    result = f'{celsius:.2f} degrees Celsius = {f:.2f} degrees Fahrenheit.'
    return result


def convert_far_to_cel(fahrenheit):
    """This function takes degrees Fahrenheit and convert them to Celsius"""

    c = ((fahrenheit - 32) * 5) / 9
    result = f'{fahrenheit:.2f} degrees Fahrenheit = {c:.2f} degrees Celsius.'
    return result


user_input1 = input('Enter a temperature in degrees F: ')
user_input1 = float(user_input1)
print(convert_far_to_cel(user_input1))

user_input2 = input('Enter a temperature in degrees C: ')
user_input2 = float(user_input2)
print(convert_cel_to_far(user_input2))
