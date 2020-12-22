from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        d1, d2 = [list(map(int, d.splitlines()[1:])) for d in s.split('\n\n')]
        d1, d2, _ = game(d1, d2)
        return sum(c * w for c, w in zip(d1 or d2, range(len(d1 or d2), 0, -1)))


def game(d1, d2):
    history = set()
    while d1 and d2:
        hsh = tuple(d1 + [0] + d2)
        if hsh in history:
            return d1, d2, 1
        history.add(hsh)
        c1, c2 = d1.pop(0), d2.pop(0)
        if len(d1) < c1 or len(d2) < c2:
            w = c1 > c2
        else:
            _, _, w = game(d1[:c1], d2[:c2])
        if w:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])
    return d1, d2, bool(d1)
