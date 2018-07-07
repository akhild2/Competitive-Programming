import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    n = len(sentence)
    l = []
    index = 0
    for i in range(n):
        if sentence[i] == "(":
            if i == opening_paren_index:
                l.append(sentence[i])
                index = len(l)
            else:
                l.append(sentence[i])
        elif sentence[i] == ")":
            if len(l) == index:
                return i
            else:
                l.pop()
    raise ValueError("Bad input! Can't delete tail node.")


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)