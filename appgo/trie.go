package main

type Trie struct {
	Children map[rune]Trie
}

func MakeNew() Trie {
	t := new(Trie)
	t.Children = make(map[rune]Trie)
	return *t
}

func (t *Trie) Insert(word string) {
	curr := *t
	for _, c := range word {
		if !curr.KeyExists(c) {
			curr.Children[c] = MakeNew()
		}
		curr = curr.Children[c]
	}
	curr.Children['$'] = MakeNew()
}

func (t *Trie) KeyExists(c rune) bool {
	curr := *t
	if _, ok := curr.Children[c]; ok {
		return true
	}
	return false
}

func (t *Trie) Search(word string) bool {
	curr := *t
	for _, c := range word {
		if !curr.KeyExists(c) { return false }
		curr = curr.Children[c]
	}
	return curr.KeyExists('$')
}

func (t *Trie) StartsWith(prefix string) bool {
	curr := *t
	for _, c := range prefix {
		if !curr.KeyExists(c) { return false }
		curr = curr.Children[c]
	}
	return true
}

func (t *Trie) AutoCompletions(prefix string) []string {
	return t.AllCompletions()
}

func (t *Trie) AllCompletions() []string {
	completions := make([]string, 0)
	curr := *t
	for k := range curr.Children {
		if k == '$' { continue }
		child := curr.Children[k]
		childCompletions := child.AllCompletions()
		if len(childCompletions) > 0 {
			for _, childCompl := range childCompletions {
				completions = append(completions, string(k) + childCompl)
			}
		} else {
			completions = append(completions, string(k))
		}
	}
	return completions
}

