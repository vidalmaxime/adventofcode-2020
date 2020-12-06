from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        groups = [len(set(x.replace('\n',''))) for x in s.split('\n\n')]
        return sum(groups)
