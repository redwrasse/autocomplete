# autocomplete.py
import time

WAR_AND_PEACE = '../war_and_peace.txt'


class Autocomplete1:
    """
    Open file and scan first 100 lines to match line
    containing input

    """

    def __init__(self):
        self.fl = open(WAR_AND_PEACE)

    def match(self, user_input):
        self.fl.seek(0)
        results = []
        if len(user_input.strip()) == 0:
            return results
        for i, ln in enumerate(self.fl):
            if i > 1000:
                break
            ln = ln.lower().strip()
            if user_input in ln:
                results.append(ln)
        return results


class Autocomplete2:
    pass


def benchmark():
    acs = [Autocomplete1]
    test_inputs = ["person", "clock", "horse", "wall", "king", "after eating"]
    for ac in acs:
        o = ac()
        start = time.time()
        for inpt in test_inputs:
            for i, c, in enumerate(inpt):
                partial_inpt = inpt[:i+1]
                res = o.match(partial_inpt)
        end = time.time()
        diff = end - start
        print(f'time: {diff}')


if __name__ == "__main__":
    benchmark()

