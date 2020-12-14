from tool.runners.python import SubmissionPy
import re


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        data = re.findall(r'(.+) = (.+)', s)
        mask0s = 0
        mask1s = 0
        mem = {}
        for instr, val in data:
            if instr == 'mask':
                mask0s = int(val.replace('X', '1'), 2)
                mask1s = int(val.replace('X', '0'), 2)
            else:
                loc = instr[4:-1]
                mem[loc] = int(val) & mask0s | mask1s
        
        return sum(mem.values())
