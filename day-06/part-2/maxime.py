from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        return sum(len(set.intersection(*(set(person) for person in group.split("\n")))) for group in s.strip().split("\n\n"))



