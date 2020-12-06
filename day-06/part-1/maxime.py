from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        return sum(len(set(group.replace("\n", ""))) for group in s.strip().split("\n\n"))
