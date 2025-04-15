letter = "Hey my name is {1} I am from {0}"
name = "Payal"
Country ="India"

print(letter.format(Country, name))
print(f"Hey my name is{name} and I am from {Country}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
#print(txt.format())
print(type(f"{2 * 30}"))