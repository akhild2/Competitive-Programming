def permute(a, l, r, permutations_list):
    if l==r:
        # print(''.join(a))
        permutations_list.append(''.join(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, permutations_list)
            a[l], a[i] = a[i], a[l]


import unittest


def get_permutations(string):
    # Generate all permutations of the input string
    if string=='':
    	return {''}
    permutations_list = []
    charArray = list(string)
    permute(charArray, 0, len(charArray)-1, permutations_list)
    return set(permutations_list)


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)