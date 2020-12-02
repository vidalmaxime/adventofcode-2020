from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n")
        valid = 0
        for line in lines:
            limits, letter, password = line.split()
            [min, max] = limits.split("-")
            if (password[int(min) - 1] == letter[0] and password[int(max) - 1] != letter[0]) or (
                    password[int(min) - 1] != letter[0] and password[int(max) - 1] == letter[0]):
                valid += 1
        return valid
