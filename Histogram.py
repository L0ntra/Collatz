def Histogram(MAX,MIN=1,NthPrime=1,factor=False):
  "Compiles \'odd\' hits of Hailstone numbers from MIN to MAX inclusive",
  "NthPrime as in func. Failstone",
  "nWARNING: LARGE VALUES BECOME COMPUTATIONALY INTENSIVE VERY QUICKLY"

    if type(MAX) != int or MAX <= 1:
        print("ERR - Histogram arg. MAX")
        return 'ERR'
    elif type(MIN) != int or MIN < 1:
        print("ERR - Histogram arg. MIN")
        return 'ERR'
    elif MIN > MAX:
        print("ERR - Hailstone args. MIN > MAX")
        return 'ERR'
    elif type(NthPrime) != int or NthPrime < 0:
        print("ERR - Histogram arg. NthPrime")
        return "ERR"
    elif NthPrime+1 > len(Primes):
        PrimeExtender(int(2*(NthPrime+1)*math.log(NthPrime+1)))
        Histogram(MAX,MIN,NthPrime)
    elif NthPrime+1 > len(Composites):
        CompsExtender(1,NthPrime)
        Histogram(MAX,MIN,NthPrime)
    else:
        Scores = [0]
        ticker = 0
        while MIN+ticker <= MAX:
            hits = Failstone(MIN+ticker,'l',NthPrime)
            if max(hits) > max(Composites[NthPrime]):
                print("extending Comps. to",max(hits))
                print("Halistone seed",MIN+ticker,"caused extension")
                CompsExtender(max(hits)+1,NthPrime)
            while len(Scores) < len(Composites[NthPrime]):
                Scores.append(0)
            while len(hits) != 0:
                Scores[Composites[NthPrime].index(hits.pop())] +=1
            ticker +=1
        skips = 0
        ticker = 0
        while ticker < len(Scores):
            if Scores[ticker] != 0:
                if skips != 0:
                    print("\tomiting",skips,"vlaues w/->0")
                    skips = 0
                if factor == False:
                    print(str(Composites[NthPrime][ticker])+"->"+str(Scores[ticker]))
                else:
                    print(Composites[NthPrime][ticker],PrimeFactorize(Composites[NthPrime][ticker],'r'),
                          "->",
                          str(Scores[ticker]))
            else:
                skips +=1
            ticker +=1

