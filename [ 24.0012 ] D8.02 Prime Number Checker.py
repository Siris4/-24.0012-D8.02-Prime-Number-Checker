# Write your code below this line 👇


def prime_checker(number):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return False
    print(f"{n} is a prime number.")
    return True

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)