docsearch
---
![](./autocomplete.gif)


### Autocomplete
Kinds of autocomplete

* Autocomplete1: Open file and scan (first seek to beginning) to match line containing input.
* Autocomplete2: Open file and store in memory line by line, run match line containing input.
* Autocomplete3: Prefix tree-based autocomplete (tbd).

### Setup

Download text resources

```
./download_text.sh
```

Launch server

```
cd server
python3 docsearch.py
```

Launch client

```
cd ui
npm start
```