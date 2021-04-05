# autocomplete.py
from trie import Trie
import os


WAR_AND_PEACE = os.path.join(os.path.dirname(__file__),
                             'war_and_peace.txt')


def clean_text(ln):
    return ln.lower().strip()


class Autocomplete:

    """ Prefix-trie based autocomplete """

    def __init__(self):
        self.fl = open(WAR_AND_PEACE)
        self.trie = Trie()
        for ln in self.fl:
            self.trie.insert(clean_text(ln))

    def match(self, user_input):
        results = []
        if len(clean_text(user_input)) == 0:
            return results
        return self.trie.autocompletions(user_input)
