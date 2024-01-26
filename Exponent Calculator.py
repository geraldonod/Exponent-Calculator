#create user defined function
def exponent(base, exp):
    num = exp
    result = 1

#create loop to get exponent
    while num > 0:
        result = result * base
        num = num - 1
    print(f"{base} raises to the power of {exp} is: {result}")

#print result
exponent(2,5)
exponent(5,4)