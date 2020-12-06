from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        groups = s.split('\n\n')
        customs = 0
        for group in groups:
            customs += len(set.intersection(*(set(p) for p in group.split('\n'))))
        return customs
