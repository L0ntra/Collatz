Composites = [[1],[1]]
def CompsExtender(number,NthPrime=1):
    "Compiles seperate lists of composites up to \'number\' for each value",
    "of \'NthPrime\' Composites in \'NthPrime\' list lack first \'NthPrime\'",
    "primes as factors"

    # Input checking
    if type(number) != int or number <= 0:
        print("ERR - CompsExtender arg. number")
        return "ERR"
    elif type(NthPrime) != int or NthPrime < 0:
        print("ERR - CompsExtender arg. NthPrime")
        return "ERR"

    if NthPrime+1 > len(Primes):
        while NthPrime+1 > len(Primes):
            PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
            CompsExtender(number,NthPrime)
    n = len(Composites)-1

    if n < NthPrime:
        ticker = 0
        while ticker <= (NthPrime - n):
            Composites.append([1])
            ticker += 1
        CompsExtender(number,NthPrime)
    elif number < max(Composites[NthPrime]):
        return
    elif NthPrime == 0:
        m = max(Composites[0])
        ticker = 0
        while m+ticker < number:
            Composites[0].append(m+ticker+1)
            ticker += 1
    else:
        m = max(Composites[NthPrime])
        ticker0 = 0
        while m+ticker0+1 <= number:
            ticker1 = 0
            Add = True
            while ticker1 < NthPrime and Add == True:
                if (m+ticker0+1) % Primes[ticker1] == 0:
                    Add = False
                    ticker1 += 1
                else:
                    ticker1 += 1
            if Add == True:
                Composites[NthPrime].append(m+ticker0+1)
                ticker0 += 1
            else:
                ticker0 += 1



Rythems = [1,[2],[4,2]]
def RhythemFinder(NthPrime):
    'under construction'
    if type(NthPrime) != int or NthPrime < 0:
        print("ERR - RhythemFinder arg. NthPrime")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
        RhythemFinder(NthPrime)
    elif len(Composites) < NthPrime-1:
        CompsExtender(12,NthPrime-1)
        RhythemFinder(NthPrime)
    elif max(Composites[NthPrime]) < Primes[NthPrime]**2+Primes[NthPrime]**3-Primes[NthPrime]:
        CompsExtender((Primes[NthPrime]**2+Primes[NthPrime]**3),NthPrime)
        RhythemFinder(NthPrime)
    else:
        print("rest of function goes here") 
