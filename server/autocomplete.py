# autocomplete.py
import time
import difflib

WAR_AND_PEACE = '../war_and_peace.txt'


def match_func1(input, line):
    return input in line



class Autocomplete1:
    """
    Open file and scan (first seek to beginning) to match line
    containing input

    """

    def __init__(self):
        self.fl = open(WAR_AND_PEACE)
        self.name = 'ac1'

    def match(self, user_input):
        self.fl.seek(0)
        results = []
        if len(user_input.strip()) == 0:
            return results
        for i, ln in enumerate(self.fl):
            ln = ln.lower().strip()
            if user_input in ln:
                results.append(ln)
        return results


class Autocomplete2:
    """ Open file and store in memory line by line, run match line containing
     input """

    def __init__(self):
        self.name = 'ac2'
        self.lines = []
        with open(WAR_AND_PEACE) as fl:
            for ln in fl:
                self.lines.append(ln)

    def match(self, user_input):
        results = []
        if len(user_input.strip()) == 0:
            return results
        for i, ln in enumerate(self.lines):
            ln = ln.lower().strip()
            if match_func1(user_input, ln):
                results.append(ln)
        return results


def benchmark():
    acs = [Autocomplete1, Autocomplete2]
    test_inputs = ["after eating", "slept for a few", "below the"]
    for ac in acs:
        o = ac()
        start = time.time()
        for inpt in test_inputs:
            for i, c, in enumerate(inpt):
                partial_inpt = inpt[:i+1]
                res = o.match(partial_inpt)
        end = time.time()
        diff = end - start
        print(f'version: {o.name} time: {diff}')


if __name__ == "__main__":
    benchmark()
