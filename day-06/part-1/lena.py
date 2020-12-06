from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        groups = s.split("\n\n")
        sum_ = 0
        for group in groups:
            sum_+=len(set(group.replace("\n","")))
        print(sum_)
        return sum_
