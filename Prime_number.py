def is_prime(n):
    sum=0
    if n <= 1:
        return -1
    for i in range(2, n):
        if n % i == 0:
            return -1
    for i in range(0,n+1):
        sum =i+sum
    return sum

print(is_prime(7))