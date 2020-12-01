from tool.runners.python import SubmissionPy
from itertools import combinations


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # Your code goes here
        entries = list(map(int, s.split()))
        for entry_1 in entries:
            if entry_1 < 2020:
                new_target = 2020 - entry_1
                for entry_2 in entries:
                    if entry_2 < new_target and (new_target - entry_2) in entries:
                        return (new_target - entry_2) * entry_1 * entry_2
