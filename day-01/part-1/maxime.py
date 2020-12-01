from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        n = {int(l) for l in s.strip().split('\n') if int(l) > 1010} & {2020 - int(l) for l in s.strip().split('\n') if int(l) <= 1010}
        return [k * (2020 - k) for k in n][0]
