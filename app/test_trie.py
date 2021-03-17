import unittest
from trie import Trie


class TestTre(unittest.TestCase):

    def setUp(self):
        pass

    def test_insert(self):
        trie = Trie()
        trie.insert('foo')
        trie.insert('fo iz')
        trie.insert('fooz')
        trie.insert('folly')
        assert 'f' in trie.d

    def test_search(self):
        trie = Trie()
        trie.insert('foo')
        assert trie.search('foo')

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


