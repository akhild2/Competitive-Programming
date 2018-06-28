import unittest


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.End_of_Word = False


def char_to_index(ch):
    return ord(ch) - ord('a')


def get_node():
    return TrieNode()


class Trie(object):

    def __init__(self):
        self.root = get_node()

    # Implement a trie and use it to efficiently store strings

    def add_word(self, word):
        if self.search(word):
            return False
        else:
            crawl = self.root
            word_length = len(word)
            for i in range(word_length):
                index = char_to_index(word[i])
                if not crawl.child[index]:
                    crawl.child[index] = get_node()
                crawl = crawl.child[index]
            crawl.End_of_Word = True
            return True

    def search(self, word):
        crawl = self.root
        word_length = len(word)
        for i in range(word_length):
            index = char_to_index(word[i])
            if not crawl.child[index]:
                return False
            crawl = crawl.child[index]
        return crawl is not None and crawl.End_of_Word


# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
