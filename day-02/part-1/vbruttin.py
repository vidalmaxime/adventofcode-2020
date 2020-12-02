from tool.runners.python import SubmissionPy
import re
from itertools import zip_longest


class VbruttinSubmission(SubmissionPy):
    def grouper(self, iterable, n):
        args = [iter(iterable)] * n
        return zip_longest(*args)

    def run(self, s):
        return sum(
            int(min_) <= pwd.count(c) <= int(max_) for min_, max_, c, pwd in self.grouper(re.split(' |-|: |\n', s), 4))
