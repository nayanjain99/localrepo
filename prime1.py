
def primeno(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False  
    for i in range(2, int(n**0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime
def primeDivision(n):
    isPrime = primeno(n)
    for i in range(2, n // 2 + 1):
        if isPrime[i] and isPrime[n - i]:
            return [i, n - i]

    return []
  
if __name__ == '__main__':

    n = int(input("Enter the number:"))
    result = primeDivision(n)
    
    print(result[0], result[1])