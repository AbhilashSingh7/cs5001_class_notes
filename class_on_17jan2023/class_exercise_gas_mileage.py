# Gas mileage program

def main():
    PRECISION = 2
    miles = float(input("Enter the number of miles: "))
    gallons = float(input("Enter the gallons of fuel used:"))
    mpg = round(miles/gallons, PRECISION)

    print(f"Miles per gallon: {mpg}")


main()
