##formula to convert celsius to fahrenheit
##(35°C × 9/5) + 32

def tempFahrenheit(celsius):
    return (celsius * 9/5)+ 32

# print(tempFahrenheit(35))
# print(tempFahrenheit(20))

c=eval(input("Enter Celsius: "))
print(tempFahrenheit(c))
