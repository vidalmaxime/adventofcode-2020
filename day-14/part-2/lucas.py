from tool.runners.python import SubmissionPy
import re


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        data = re.findall(r'(.+) = (.+)', s)
        mask = ''
        mem = {}
        for instr, val in data:
            if instr == 'mask':
                mask1s = int(val.replace('X', '0'), 2)
                mask = val
            else:
                loc = int(instr[4:-1])
                locs = [loc | mask1s]
                idxs = (idx for idx, x in enumerate(reversed(mask)) if x == 'X')
                for i in idxs:
                    temp_locs = [loc & ~(1 << i) for loc in locs]
                    temp_locs += [loc | (1 << i) for loc in locs]
                    locs = temp_locs
                mem = {**mem, **{loc: int(val) for loc in locs}}
        
        return sum(mem.values())
    