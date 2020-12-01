from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        numbers = {int(l) for l in s.strip().split('\n')}
        return [(x * y * (2020 - x - y)) for x in numbers for y in numbers if (2020 - x - y) in numbers][0]
