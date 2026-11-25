name = input("What is your name? ")

print("Hello " + name)
print("Your name has " + str(len(name)) + " Letters.")
print(name.upper())
print(name.lower())
print(name.capitalize())

if name.lower() == "batman":
    print("Welcome back, Dark Knight.")
elif name.lower() == "simon":
    print("Hello Simon, the builder begins.")
else:
    print("Nice to meet you.")
try:
    age = input("how old are you? ")
    years_to_100 = 100 - age 
print(f"You will turn 100 in {years_to_100} years.")
except:
print("please enter your age using numbers.")