from tool.runners.python import SubmissionPy
import re

class LenaSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split('\n')
        mask = None
        memory = {}
        for instruction in lines:
            if instruction.startswith('mem'):
                address, value = re.findall('mem\[(\d+)\] = (\d+)', instruction)[0]
                masked_value = ''.join([v if m == 'X' else m for m, v in zip(mask, format(int(value), '036b'))])
                memory[address] = ''.join(masked_value)
            else:
                mask = re.findall('mask = ([10X]{36})', instruction)[0]
        return sum([int(value, 2) for _, value in memory.items()])

