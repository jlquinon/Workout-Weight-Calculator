"""This module contains a function to convert a weight measurement to plates used in a gym"""

def weight_to_plate(weight):
    """Converts the inputted weight into a form in lifting plates"""
    weight -= 45    #Subtract typical bar weight
    plate45 = 0
    plate35 = 0
    plate25 = 0
    plate10 = 0
    plate5 = 0
    plate2_5 = 0

    while weight/(2*45):
        weight -= (2*45)
        plate45 += 1

    while weight/(2*35):
        weight -= (2*35)
        plate35 += 1

    while weight/(2*25):
        weight -= (2*25)
        plate25 += 1

    while weight/(2*10):
        weight -= (2*10)
        plate10 += 1

    while weight/(2*5):
        weight -= (2*5)
        plate5 += 1

    while weight/(2*2.5):
        weight -= (2*2.5)
        plate2_5 += 1

    if plate45:
        print("{} 45s".format(plate45))
    if plate35:
        print("{} 35s".format(plate35))
    if plate25:
        print("{} 25s".format(plate25))
    if plate10:
        print("{} 10s".format(plate10))
    if plate5:
        print("{} 5s".format(plate5))
    if plate2_5:
        print("{} 2.5s".format(plate2_5))

def main():
    """Main function"""
    weight = input("Number: ")
    weight_to_plate(weight)

if __name__ == '__main__':
    main()
