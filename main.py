# get input
num = int( input() )

# validate the input
if num < 11 or num > 99:
    print('Input must be 11-99')
else:
    while True:
        #show the number
        print (num)

        # check to see if the digits match
        left_digit = num // 10     # // means integer division - decimals are dropped
        right_digit = num % 10     # % means modulus, which means remainder

        if left_digit == right_digit:
            break
        else:
            num = num - 1
