
class Trie:

    """ standard methods: insert, search, startsWith """

    def __init__(self):
        self.d = {}

    @staticmethod
    def from_dict(d):
        trie = Trie()
        trie.d = d
        return trie

    def __str__(self):
        return str(self.d)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.d == other.d

    def insert(self, word):
        curr = self.d
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['$'] = {}  # end of word marker

    def search(self, word):
        curr = self.d
        for c in word:
            if c not in curr: return False
            curr = curr[c]
        return '$' in curr

    def startswith(self, word):
        curr = self.d
        for c in word:
            if c not in curr: return False
            curr = curr[c]
        return True

    def autocompletions(self, prefix):
        # an additional method: autocompletion
        completions = []
        curr = self.d
        for c in prefix:
            if c not in curr: return completions
            curr = curr[c]
        # dfs rest of tree
        completions = self.__all_completions(curr)
        return [prefix + cpl for cpl in completions]

    def __all_completions(self, curr):
        # (also an additional method)
        # should make iterative instead of recursive
        completions = []
        for k in curr:
            if k == '$': continue
            child_completions = self.__all_completions(curr[k])
            if child_completions:
                for child_c in child_completions:
                    completions.append(k + child_c)
            else:
                completions.append(k)
        return completions

    def serialize(self):
        enc = []

        def pre_enc(node):
            c, curr = node
            if c == '$':
                enc.append(str(1))
                enc.append(c)
            else:
                n_ch = len(curr)  # num. of children
                enc.append(str(n_ch))  # encode num. of children for decoding
                enc.append(c)
                for child_c, child_d in curr.items():
                    child_node = child_c, curr[child_c]
                    pre_enc(child_node)

        root = '*', self.d
        pre_enc(root)
        return ''.join(enc)

    @staticmethod
    def deserialize(data):

        enc_data = list(data)

        def pre_dec(enc):
            if not enc: return {}
            n_ch = int(enc.pop(0))
            c = enc.pop(0)
            if c == '$': return {'$': {}}
            curr = {c: {}}
            for i in range(n_ch):
                child_d = pre_dec(enc)
                curr[c].update(child_d)
            return curr

        d = pre_dec(enc_data)['*']
        return Trie.from_dict(d)




