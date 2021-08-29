import math

def determine_if_square(root):
    if (math.floor(root) == root):
        return True
    return False

def determine_if_prime(n, root):
    for prime in primes_list:
        if (prime >= root):
            return True
        divisor = n/prime
        if (math.floor(divisor) == divisor):
            # this is a factor
            return False

def squarest_factor(n, root):
    starting_val = math.floor(root)
    for i in range(starting_val, 1, -1):
        divisor = n/i
        if (math.floor(divisor) == divisor):
            return i

if __name__ == '__main__':
    squareness_list = [1, 1] # squareness of 0 and 1 (special cases)
    squarest_factor_list = ["0", "1"]
    primes_list = [2] # list of primes we've found so far
    rename_me = 1000000
    for n in range(2, rename_me):
        root = math.sqrt(n)
        if (determine_if_square(root)):
            squareness_list.append(1)
            squarest_factor_list.append("square")
            continue

        if (determine_if_prime(n, root)):
            if (n != 2):
                primes_list.append(n)
            squareness_list.append(1.0/root)
            squarest_factor_list.append("prime")
            continue

        # so this is a non-square composite number
        i = squarest_factor(n, root)
        squareness_list.append(i/root)
        squarest_factor_list.append(str(i))
    for index, val in enumerate(squareness_list):
        print(str(index) + " " + str(val) + " " + squarest_factor_list[index])
    #print(primes_list)
