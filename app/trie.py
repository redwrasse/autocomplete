
class Trie:

    """ standard methods: insert, search, startsWith """

    def __init__(self):
        self.d = {}

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

        def pre_enc(c, curr):
            enc.append(c)
            if c != '$':
                for ch in curr:
                    pre_enc(ch, curr[ch])

        pre_enc('', self.d)
        return ''.join(enc)

    def deserialize(self, data):
        enc = list(data)
        # big problem: can't serialize /deserialized preorder if don't know
        # number of children for a given node.
        def pre_dec(enc):
            c = enc.pop(0)
            if c == '$':
                return {'$': {}}
            curr = { c: {}}
            left = pre_dec(enc) # this isn't correct, there are multiple children
            right = pre_dec(enc)
            curr[c] = {**left, **right}
            return curr

        return pre_dec(enc)


