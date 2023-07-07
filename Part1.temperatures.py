temp = int(input("Please type in a temperature (F): "))
convert = float((temp - 32) * (5/9))
if convert >= 0:
    print(temp, "degrees Fahrenheit equals", convert, "degrees Celsius")

elif convert < 0:
    print(temp, "degrees Fahrenheit equals", convert, "degrees Celsius")
    print("Brr! It's cold in here!")