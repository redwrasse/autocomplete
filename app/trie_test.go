package main

import (
	"testing"
)

func SampleTrie() Trie {
	t := MakeNew()
	t.Insert("foo")
	t.Insert("fo iz")
	t.Insert("foozy")
	return t
}


func TestTrie_Insert(t *testing.T) {
	trie := SampleTrie()
	trie.Insert("bar")
}

func TestTrie_KeyExists(t *testing.T) {
	trie := SampleTrie()
	if !trie.KeyExists('f') {
		t.Fail()
	}
}

func TestTrie_Search(t *testing.T) {
	trie := SampleTrie()
	if !trie.Search("foozy") {
		t.Fail()
	}
}

func TestTrie_StartsWith(t *testing.T) {
	trie := SampleTrie()
	if !trie.StartsWith("fo") {
		t.Fail()
	}
}

func TestTrie_AutoCompletions(t *testing.T) {
	trie := SampleTrie()
	autoCompletions := trie.AutoCompletions("fo")
	if !SliceContains(autoCompletions, "foozy") { t.Fail() }
	if !SliceContains(autoCompletions, "fo iz") { t.Fail() }
}

func SliceContains(sl []string, e string) bool {
	for _, v := range sl {
		if v == e { return true }
	}
	return false
}