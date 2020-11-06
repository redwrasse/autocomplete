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
    """
    Open file and store in memory line by line, run match line
    containing input
    """

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


class Autocomplete3:

    """ Same as version 2 but refine down list for each
    incremental input. First stateful autocomplete."""

    def __init__(self):
        self.name = 'ac3'
        self.lines = []
        self.reset_lines()
        self.previous_user_input = None

    def reset_lines(self):
        self.lines = []
        with open(WAR_AND_PEACE) as fl:
            for ln in fl:
                self.lines.append(ln)

    def match(self, user_input):
        if self.previous_user_input is not None and \
                user_input[:-1] != self.previous_user_input:
            self.reset_lines()
        results = []
        updated_lines = []
        if len(user_input.strip()) == 0:
            return results
        for i, ln in enumerate(self.lines):
            ln = ln.lower().strip()
            if match_func1(user_input, ln):
                results.append(ln)
                updated_lines.append(ln)
        self.lines = updated_lines
        self.previous_user_input = user_input
        return results


class Autocomplete4:
    """ Prefix tree-based autocomplete """

    def __init__(self):
        self.state = None

    def match(self, user_input):
        pass


def benchmark():
    # doesn't work as implemented for ac3 because it is stateful
    acs = [Autocomplete1, Autocomplete2, Autocomplete3]
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
        print(f'version: {o.name} time: {diff}s')


if __name__ == "__main__":
    benchmark()
