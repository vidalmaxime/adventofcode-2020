from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        groups = s.split("\n\n")
        sum_ = 0
        for group in groups:
            sets = []
            for person in group.split("\n"):
                sets.append(set(person))
            same = set.intersection(*sets)
            sum_+=len(same)
        print(sum_)
        return sum_