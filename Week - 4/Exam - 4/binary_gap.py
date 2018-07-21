test_cases = int(input('Enter number of test cases : '))
for test_case in range(test_cases):
    decimal = int(input())
    binary = '{0:b}'.format(decimal)
    if decimal < 0:
        limit = len('{0:b}'.format(decimal))
        binary = ('{0:b}'.format(decimal + (1 << 32)))[-limit:]
    print(binary)
    answer = binary.split('0')
    print(answer)
    print(len(max(answer)))
