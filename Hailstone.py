def Hailstone(number, factor = False):
    "Sends the input number through the HailStone function"

    # Error Checking
    if type(number) != int or number <=0:
        print("ERR - HailStone arg. number")
        return "ERR"
    elif type(factor) != bool:
        print("ERR - HailStone arg. factor")
        return "ERR"

    # Hailstone Algorithm
    while number != 1:
        if number % 2 == 0:
           number = int(number/2)
        else:
            number = int((number*3)+1)

        if factor == True:
            PrimeFactorize(number)
        else:
            print(number)
