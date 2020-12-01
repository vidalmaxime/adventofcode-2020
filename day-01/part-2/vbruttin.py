from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # Your code goes here
        entries = list(map(int, s.split()))
        for entry in entries:
            for entry_2 in entries:
                if (opposite_entry := 2020 - entry - entry_2) in entries:
                    return opposite_entry * entry * entry_2
