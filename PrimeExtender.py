# Expand Primes
Primes = [2,3,5,7,11]            
def PrimeExtender(number):
    "Find all primes less than \'number\' and add them to Primes"

    if number < max(Primes):
        return
    else:
        print('Extending Primes...')
        if int(number + 2*math.log(number))+1 < int(len(Primes)*math.log(len(Primes)))+2:
            siftMax = int(len(Primes)*math.log(len(Primes)))+2
        else:
            siftMax = int(number + 2*math.log(number))+1
        siftMin = max(Primes) + 1
        siftRange = siftMax-siftMin

        if int(siftMax**(1/2)) > max(Primes):
            PrimeExtender(int(siftMax**(1/2))+1)

        #Set up the boolian list to be sifted
        Sifter = []
        ticker = 0
        while ticker < siftRange:
            Sifter.append(1)
            ticker += 1
            
        #populate the list of primes to use as sieve
        Sieve = []
        ticker = 0
        while int(siftMax**(1/2)) > Primes[ticker]:
            Sieve.append(Primes[ticker])
            ticker = ticker +1

        #do the sifting
        ticker0 = 0
        while ticker0 < len(Sieve):
            ticker1 = 0
            Correction = siftMin%Sieve[ticker0]
            while ticker1*Sieve[ticker0] + siftMin - Correction < siftMax:
                if ticker1 == 0 and Correction != 0:
                    pass
                else:
                    Sifter[ticker1*Sieve[ticker0]-Correction] = 0
                ticker1 +=1
            ticker0 +=1

        #add new primes to list
        ticker = 0
        found = 0
        while ticker < siftRange:
            if Sifter[ticker] == 1:
                Primes.append(siftMin+ticker)
                found +=1
            else:
                pass
            ticker +=1
        print('Found '+str(found)+' new Primes!')

