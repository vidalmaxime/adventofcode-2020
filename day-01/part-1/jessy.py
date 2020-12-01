from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        entries = list(map(int, s.split()))
        for n, entry in enumerate(entries[:-1], start=1):
            comp = 2020 - entry
            if comp in entries[n:]:
                return entry * comp

