from math import sqrt
def PrimeFactorize(num, output='p'):
    '''Finds the prime factors of the input number",
       output = p : print factorization
              | r : return divisors list
    '''
    
    # Input checking
    if type(nu) != int or num <= 0:
        print("ERR - PrimeFactorize arg. num")
        return 'ERR'
    if output not in ['p','r']:
        print("ERR - PrimeFactorize arg. output")
        return "ERR"

    num2root = int(sqrt(n))
    if (num2root + 1) >= max(Primes):
        PrimeExtender(num2root + 1)
        PrimeFactorize(num, output) # Recursion forces input checking on known
                                    # good values.
                                    # What does this even do?
    else:
        n = num
        Divisors = []
        ticker = 0

        while True:
            n2root = int(sqrt(n))
            if (n2root + 1) < Primes[ticker]:
                Divisors.append([int(n), 1])
                break; # n is prime or 1 stop looping
                
            elif n % Primes[ticker] == 0:
                found = [Primes[ticker], 0]

                while n % Primes[ticker] == 0: # Factor out the prime
                    n = n / Primes[ticker]
                    found[1] = found[1] + 1    # Record the power of the prime
                
                Divisors.append(found)         # Add pime to the list...
                ticker = 0
                
            else:
                ticker += 1
        
        if output == 'p':
            print(str(num)+' ',Divisors)
        else:
            return Divisors


 def main():
   return

