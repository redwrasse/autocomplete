package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

type HttpTrieHandler struct {
	t Trie
}


func InitializeTrieHandler() HttpTrieHandler {
	trieHandler := HttpTrieHandler{MakeNew()}
	MakeWarAndPeaceTrie(trieHandler.t)
	return trieHandler
}

func (HTH HttpTrieHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {

	// expects url /?prefix=<prefix>
	fmt.Println("GET params: ", r.URL.Query())

	prefix := r.URL.Query().Get("prefix")

	p := CleanLine(string(prefix))
	fmt.Println("Read prefix: ", p)
	fmt.Println("Autocompleting on %s", p)
	completions := HTH.t.AutoCompletions(p)
	//fmt.Printf("%v\n", completions)
	json.NewEncoder(w).Encode(completions)
	fmt.Println("called autocomplete handler, returning %d completions", len(completions))
}

func main() {

	trieHandler := InitializeTrieHandler()
	fmt.Printf("%v\n", trieHandler.t.AutoCompletions("za"))
	////log.Fatal(http.ListenAndServe(":8080", trieHandler))

}

func MakeWarAndPeaceTrie(t Trie) {

	file, err := os.Open("./war_and_peace.txt")
	if err != nil { log.Fatal(err) }
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {

		s := CleanLine(scanner.Text())
		if len(s) > 0 {
			//fmt.Println(s)
			t.Insert(s)
		}
	}

	if err := scanner.Err(); err != nil { log.Fatal(err) }

}

func CleanLine(s string) string {
	return strings.ToLower(strings.Join(strings.Fields(strings.TrimSpace(s)), " "))
}

func ExampleTrie() {

	t := MakeNew()
	t.Insert("foo")
	t.Insert("fo iz")
	t.Insert("foozy")
	t.Search("foo")
	println(t.Search("fooz"))
	println(t.Search("oaf"))
	println(t.Search("foo"))
	fmt.Printf("%v\n", t.AutoCompletions("fo"))

}
