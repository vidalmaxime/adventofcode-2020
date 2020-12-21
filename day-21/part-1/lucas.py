from tool.runners.python import SubmissionPy

# inspiration from https://github.com/ephemient/aoc2020/tree/main/py/src/aoc2020

class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        lhss = []
        mapping = {}
        for line in s.splitlines():
            lhs, rhs = line.rstrip().split(' (contains ', maxsplit=1)
            lhs = lhs.split()
            lhss.append(lhs)
            for k in rhs.rstrip(')').split(', '):
                if k in mapping:
                    mapping[k].intersection_update(lhs)
                else:
                    mapping[k] = set(lhs)        
        exclude = set(v for vs in mapping.values() for v in vs)
        return sum(v not in exclude for lhs in lhss for v in lhs)
