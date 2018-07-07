t = int(input('Enter the number of test cases : '))
for i in range(t):
    first_string = input().lower()
    second_string = input().lower()
    alphabets = [0]*26
    for char in first_string:
        if not char == ' ':
            alphabets[ord(char) - 97] += 1
    for char in second_string:
        if not char == ' ':
            alphabets[ord(char) - 97] -= 1

    print(alphabets == [0]*26)
