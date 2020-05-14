def check_prime(x):
    flag = False
    if x > 2:
        for n in range(2, x):
            if x % n == 0:
                print("%r is not a prime no.." % x)
            else:
                print("%r is a prime no.." % x)
            break
    elif x == 2:
        print("2 is a prime no.")
    else:
        print("Not prime.")


num = int(input("Enter a NUmber: "))
check_prime(num)
