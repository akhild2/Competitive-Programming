morse_code_dictionary = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'}

# ['gin', 'zen', 'gig', 'msg']

t = int(input('Enter the number of test cases : '))
for i in range(t):
    input_words = eval(input())
    output = 0
    answer = {}
    for word in input_words:
        resultant_string = ''
        for char in word:
            resultant_string = resultant_string + morse_code_dictionary[(char.upper())]
        if answer.get(resultant_string) is not None:
            pass
        else:
            output += 1
            answer[resultant_string] = 0
    print(output)
