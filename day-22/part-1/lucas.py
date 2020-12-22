from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        d1, d2 = [list(map(int, d.splitlines()[1:])) for d in s.split('\n\n')]

        while d1 and d2:
            c1, c2 = d1.pop(0), d2.pop(0)
            if c1 > c2:
                d1.extend([c1, c2])
            else:
                d2.extend([c2, c1])
        
        return sum(c * w for c, w in zip(d1 or d2, range(len(d1 or d2), 0, -1)))
