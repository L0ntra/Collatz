def PrimeFactorize(number,output='p'):
    "Finds the prime factors of the input number",
    "output = \'p\', print factorization, \'r\', return divisors list"

    if type(number) != int or number <= 0:
        print("ERR - PrimeFactorize arg. number")
        return 'ERR'
    elif output not in ['p','r']:
        print("ERR - PrimeFactorize arg. output")
        return "ERR"
    elif int(number**(1/2))+1 >= max(Primes):
        PrimeExtender(int(number**(1/2))+1)
        PrimeFactorize(number,output)
    else:
        n = number
        Divisors = []
        ticker = 0
        while n != 1:

            if int(n**(1/2))+1 < Primes[ticker]:
                prime = [int(n),1]
                Divisors.append(prime)
                n = 1
                
            elif n % Primes[ticker] == 0:
                find = [Primes[ticker],0]
                while n % Primes[ticker] == 0:
                    n = n / Primes[ticker]
                    find[1] = find[1] + 1
                Divisors.append(find)
                ticker = 0
                
            else:
                ticker += 1
        
        if output == 'p':
            print(str(number)+' ',Divisors)
        else:
            return Divisors
