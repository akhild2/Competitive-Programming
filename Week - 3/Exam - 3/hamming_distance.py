def compare(bin_1, bin_2):
    print('binary value of x = '+bin_1)
    print('binary value of y = '+bin_2)
    distance = 0
    for i in range(len(bin_1)):
        if bin_1[i] != bin_2[i]:
            distance += 1
    return distance


test_cases = int(input('Enter the number of test cases : '))
for test in range(test_cases):
    x = int(input('Enter value of X : '))
    y = int(input('Enter value of Y : '))
    x = "{0:b}".format(x)
    y = "{0:b}".format(y)
    if len(x) == len(y):
        print(compare(x, y))
    elif len(x) > len(y):
        difference_of_zeros = len(x) - len(y)
        y = '0' * difference_of_zeros + y
        print(compare(x, y))
    else:
        difference_of_zeros = len(y) - len(x)
        x = '0' * difference_of_zeros + x
        print(compare(x, y))
