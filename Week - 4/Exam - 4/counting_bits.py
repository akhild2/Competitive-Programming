test_cases = int(input('Enter number of test cases : '))
for test_case in range(test_cases):
    n = int(input())
    answer = []
    for i in range(n+1):
        decimal = i
        binary = '{0:b}'.format(decimal)
        count = binary.count('1')
        # print(str(i)+' = '+str(count))
        answer.append(count)
    print(answer)
