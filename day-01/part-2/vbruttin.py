from tool.runners.python import SubmissionPy
from itertools import combinations


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # Your code goes here
        entries = list(map(int, s.split()))
        for entry, entry_2 in combinations(entries, 2):
            if (opposite_entry := 2020 - entry - entry_2) in entries:
                return opposite_entry * entry * entry_2
