# User input

age = int(input('What is your age?'))
if age < 65:
    r_age = 65 - age
    print("You can retire in {0} years.".format(r_age))
else:
    print("You are retired!")
