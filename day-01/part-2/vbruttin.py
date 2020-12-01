from tool.runners.python import SubmissionPy
from itertools import combinations


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # Your code goes here
        entries = list(map(int, s.split()))
        for entry_1 in entries:
            if (new_target := 2020 - entry_1) > 0:
                for entry_2 in entries:
                    if (final_target := new_target - entry_2) > 0:
                        if (opposite_entry := final_target) in entries:
                            return opposite_entry * entry_1 * entry_2
