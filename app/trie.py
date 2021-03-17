
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

