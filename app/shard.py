# autocomplete.py
from trie import Trie
import os


WAR_AND_PEACE = os.path.join(os.path.dirname(__file__),
                             'war_and_peace.txt')


def clean_text(ln):
    return ln.lower().strip()


def shard_from_file(fl, start, end):
    """ build shard for lines starting in range
    [start, end] """
    trie = Trie()
    for ln in fl:
        clean_ln = clean_text(ln)
        if start <= clean_ln <= end:
            trie.insert(clean_ln)
    return trie


def shard_from_trie(trie, start, end):
    """ get a shard from the existing trie in memory """
    return Trie.from_dict(
        {c: child for c, child in trie.d.items()
            if start <= c <= end})


class Shard:

    """ A prefix-trie shard """

    def __init__(self, start, end):
        with open(WAR_AND_PEACE) as fl:
            self.trie = shard_from_file(fl, start, end)

    def match(self, user_input):
        results = []
        if len(clean_text(user_input)) == 0:
            return results
        return self.trie.autocompletions(user_input)
