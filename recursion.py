# factorials are like this 5! = 5 × 4 × 3 × 2 × 1 = 120
# which means that the function calls it self until 1

def fact(x):
    # the base case
    if x == 1:
        return 1
    # recursive case
    # it calls the fact function until the number is equal to 1
    else:
        return x * fact(x-1)
    