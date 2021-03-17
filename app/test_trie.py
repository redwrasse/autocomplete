import unittest
from trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.mock_trie = Trie()
        self.mock_trie.insert('foo')
        self.mock_trie.insert('bar')
        self.mock_trie.insert('foz')

    def test_insert(self):
        trie = Trie()
        trie.insert('foo')
        trie.insert('fo iz')
        trie.insert('fooz')
        trie.insert('folly')
        assert 'f' in trie.d

    def test_search(self):
        assert self.mock_trie.search('foo')

    def test_startswith(self):
        trie = Trie()
        trie.insert('foo')
        assert trie.startswith('fo')

    def test_autocompletions(self):
        trie = Trie()
        trie.insert('foo')
        trie.insert('fo iz')
        trie.insert('fooz')
        trie.insert('folly')
        expected = ['fooz', 'fo iz', 'folly']
        result = trie.autocompletions('fo')
        assert result == expected

    def test_serialize(self):
        actual = self.mock_trie.serialize()
        expected = '2*1f2o1o1$1z1$1b1a1r1$'
        assert actual == expected, \
            print(f'should have encoded to {expected}, got {actual}')

    def test_deserialize(self):
        expected = self.mock_trie
        actual = Trie.deserialize(self.mock_trie.serialize())
        assert actual == expected, \
            print(f'incorrect deserialization. '
                  f'expected {expected}, got {actual}')



