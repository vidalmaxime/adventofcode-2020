from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n")
        valid = 0
        for line in lines:
            limits, letter, password = line.split()
            [min, max] = limits.split("-")
            if int(min) <= password.count(letter[0]) <= int(max):
                valid += 1
        return valid
