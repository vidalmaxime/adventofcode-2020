from tool.runners.python import SubmissionPy
# from collections import deque
from itertools import combinations


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        self.sequence = list(map(int, s.split('\n')))

        for i in range(len(self.sequence) - 26):
            target = self.sequence[i + 25]
            for s in combinations(self.sequence[i:i + 25], 2):
                if sum(s) == target:
                    break
            else:
                return target

    # Sadly marginally slower
    #     for numbers, target in zip(self.window(n=25), self.sequence[25:]):
    #         for s in combinations(numbers, 2):
    #             if sum(s) == target:
    #                 break
    #         else:
    #             return target

    # def window(self, n=2):
    #     it = iter(self.sequence)
    #     win = deque((next(it, None) for _ in range(n)), maxlen=n)
    #     yield win
    #     append = win.append
    #     for e in it:
    #         append(e)
    #         yield win