from tool.runners.python import SubmissionPy
from operator import itemgetter

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
        
        ret = []
        while True:
            for k, vs in mapping.items():
                if len(vs) == 1:
                    v = next(iter(vs))
                    ret.append((k, v))
                    mapping.pop(k)
                    for vs in mapping.values():
                        vs.discard(v)
                    break
            else:
                break
        assert not mapping
        ret.sort(key=itemgetter(0))
        return ','.join(map(itemgetter(1), ret))
