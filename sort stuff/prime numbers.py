

def prvocisla(n):

    primes = []

    for i in range(2, n + 1):

        for j in range(2, int(i ** 0.5) + 1):

            if i%j == 0:

                break

        else:

            primes.append(i)

    return primes



seznam_prvocisel = prvocisla(10000000000)

print(seznam_prvocisel)