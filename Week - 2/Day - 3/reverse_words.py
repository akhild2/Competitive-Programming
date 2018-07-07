import unittest


def reverse_words(message):

    # Decode the message by reversing the words

    i = 0
    while (len(message) - 2*i) > 1 :
        temp = message[i]
        message[i] = message[-i-1]
        message[-i-1]=temp
        i += 1

    i = 0
    while  i < len(message):
        j = i
        while j < len(message) and message[j] != ' ':
            j += 1
        k = 0
        while (j-i-2*k) > 1 :
            temp = message[i+k]
            message[i+k]=message[j-k-1]
            message[j-k-1]=temp
            k =k+1
        i = j+1
















# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)