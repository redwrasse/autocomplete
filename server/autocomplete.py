# autocomplete.py
import timeit

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
    test_inputs = ["the"]
    for ac in acs:
        o = ac()
        # TODO("time snippet")
        for inpt in test_inputs:
            res = o.match(inpt)
            print(f'results:\n{res}')


if __name__ == "__main__":
    benchmark()

