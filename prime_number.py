import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print(is_prime(25))

### Time complexity: O(sqrt(n)), Space complexity O(1)