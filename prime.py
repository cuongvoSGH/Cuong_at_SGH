# Cuong Vo - 131116
# Algorithms 
# Step 1: Define isPrime(n) function for Prime checking 
#   Step 1.1: For loops from 2 to square root of n (checking number)
#   Step 1.2: If n mod i = 0 mean n is not prime number --> return 0, break
#   Step 1.3: End For loops return 1 --> n is prime number
# Step 2: Using While loops for 2 variance i and j, j is counting variance, break when j = n (j start from 0), i is running variance for number checking

# Import package Math for function sqrt (square root)
import math

# Step 1: Define isPrime(n) function
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return 0
    return 1

# Input n from terminal, using input() method
n = int(input())

# Inital code for i = 2 (Prime number is the number that higher than 1), j = 0 for counting variance
i=2
j=0

# While loops for checking first N prime
while j < n:
    if isPrime(i):
        print(i, end =' ')
        j += 1
        i += 1
    else: 
        i += 1

