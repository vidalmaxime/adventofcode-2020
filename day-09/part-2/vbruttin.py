from tool.runners.python import SubmissionPy
from itertools import combinations


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        sequence = list(map(int, s.split('\n')))
        length = len(sequence)
        for i in range(length - 26):
            target = sequence[i + 25]
            for s in combinations(sequence[i:i + 25], 2):
                if sum(s) == target:
                    break
            else:
                break
        # target = 31161678
        for i in range(length):
            stack = sequence[i]
            for j in range(i + 1, length):
                stack += sequence[j]
                if stack > target:
                    break
                elif stack == target:
                    return min(sequence[i:j + 1]) + max(sequence[i:j + 1])
