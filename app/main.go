package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
)

type HttpBody struct {
	userInput string
}

type AutoCompleteResp struct {
	matches []string
}


func AutoCompleteHandler(t *Trie) func(w http.ResponseWriter,
	r *http.Request) {
		if t == nil {
			panic("nil Trie")
		}
		return func(w http.ResponseWriter, r *http.Request) {

			b, err := ioutil.ReadAll(r.Body)
			defer r.Body.Close()

			buf, bodyErr := ioutil.ReadAll(r.Body)
			if bodyErr != nil {
				log.Print("bodyErr ", bodyErr.Error())
				http.Error(w, bodyErr.Error(), http.StatusInternalServerError)
				return
			}

			rdr1 := ioutil.NopCloser(bytes.NewBuffer(buf))
			rdr2 := ioutil.NopCloser(bytes.NewBuffer(buf))
			log.Printf("BODY: %q", rdr1)
			r.Body = rdr2


			if err != nil {
				//http.Error(w, err.Error(), 500)
			}
			fmt.Printf("%v\n", b);
			var bdy HttpBody
			err = json.Unmarshal(b, &bdy)
			if err != nil {
				//http.Error(w, err.Error(), 500)
				//return
			} else {
				fmt.Printf("Received user input %v\n", bdy.userInput)

			}


			enableCors(&w)

			prefix := r.URL.Query().Get("prefix")

			p := CleanLine(string(prefix))
			fmt.Println("Read prefix: ", p)
			fmt.Printf("Autocompleting on %v\n", p)
			completions := t.AutoCompletions(p)
			//fmt.Printf("%v\n", completions)
			acResp := AutoCompleteResp{completions}
			json.NewEncoder(w).Encode(acResp)
			fmt.Printf("called autocomplete handler, returning %v completions\n", len(completions))
		}
}



//!!! for testing only
func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}



func main() {

	t := MakeNew()
	MakeWarAndPeaceTrie(t)

	mux := http.NewServeMux()
	mux.HandleFunc("/search", AutoCompleteHandler(&t))
	log.Fatal(http.ListenAndServe(":8080", mux))

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

