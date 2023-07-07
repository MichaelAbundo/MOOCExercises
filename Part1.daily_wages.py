wages = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
week = str(input("Day of the week: "))
if week == "Sunday":
    print("Daily wages:",((wages*2) * hours), "euros")
else:
    print("Daily wages:",(wages * hours), "euros")