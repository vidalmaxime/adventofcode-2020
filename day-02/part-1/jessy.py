from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        valid = 0
        for row in s.split('\n'):
            lims, char, passw = row.split()
            min_, max_ = map(int, lims.split('-'))
            if min_ <= passw.count(char[0]) <= max_:
                valid += 1
        return valid
