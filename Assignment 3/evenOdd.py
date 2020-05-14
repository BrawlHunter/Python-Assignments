def even_odd(num):
    if int(num) % 2 == 0:
        print("%r is an even number" % num)
    else:
        print("%r is an odd number" % num)


num1 = input("Enter a number")
even_odd(num1)
