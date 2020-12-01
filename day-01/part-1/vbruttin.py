from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # Your code goes here
        entries = list(map(int, s.split()))
        for entry in entries:
            if entry < 2020 and (opposite_entry := 2020 - entry) in entries:
                return opposite_entry * entry
