package main

import "fmt"

func main() {

	t := MakeNew()
	t.Insert("foo")
	t.Insert("fo iz")
	t.Insert("foozy")
	t.Search("foo")
	println(t.Search("fooz"))
	println(t.Search("oaf"))
	fmt.Printf("%v\n", t.AutoCompletions("fo"))

}

