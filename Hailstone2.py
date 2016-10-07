
def Failstone(number,factor=1,NthPrime=1):
    "Advanced Hailstone function"
    "number   = starting value",
    "factor   = 0 Factor none",
    "         | 1 'odd' only", 
    "         | 2 factor all", 
    "         | L return list of odds",
    "NthPrime = divide 1st -> Nth prime, multiply Nth+1 prime +1"

    if type(number) != int or number <= 0:
        print("ERR - Failstone arg. number")
        return "ERR"
    elif type(NthPrime) != int or NthPrime <= 0:
        print("ERR - Failstone arg. NthPrime")
        return "ERR"
    elif factor not in [0,1,2,'l']:
        print("ERR - Failstone arg. factor")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
        Failstone(number,factor,NthPrime)
    else:
        if factor != 'l':
            print("Removing primes ",Primes[0:NthPrime])
            print("Jump opperation = n *",Primes[NthPrime],"+ 1")
        if factor == 'l':
            odds = []
        fault = True
        while fault == True:
            ticker = 0
            while ticker < NthPrime:
                if number % Primes[ticker] == 0:
                    if factor == 0: #Print statments for 'even' case
                        print(number)
                    elif factor == 1:
                        print(number)
                    elif factor == 2:
                        PrimeFactorize(number)
                    elif factor == 'l':
                        pass
                    number = int(number/Primes[ticker])
                else:
                    ticker += 1
            if number != 1:
                if factor == 0: #Print statments for 'odd' case
                    print(number)
                elif factor == 1:
                    PrimeFactorize(number)
                elif factor == 2:
                    PrimeFactorize(number)
                elif factor == 'l':
                    odds.append(number)
                number = number*Primes[ticker] + 1
            else:
                if factor == 0: #Print statments for 1
                    print(number)
                elif factor == 1:
                    PrimeFactorize(number)
                elif factor == 2:
                    PrimeFactorize(number)
                elif factor == 'l':
                    odds.append(number)
                    return odds
                fault = False
