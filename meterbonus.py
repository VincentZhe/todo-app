feet_inches =input("Enter feet and inches:")

def parse(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
result = convert(f, i)

if result < 1:
    print('Good')
else:
    print('Bad')    