from tool.runners.python import SubmissionPy
import re
from itertools import zip_longest


class VbruttinSubmission(SubmissionPy):
    def grouper(self, iterable, n):
        args = [iter(iterable)] * n
        return zip_longest(*args)

    def run(self, s):
        return sum((pwd[int(p1) - 1] == c) ^ (pwd[int(p2) - 1] == c)
                   for p1, p2, c, pwd in self.grouper(re.split(' |-|: |\n', s), 4))
