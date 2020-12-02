from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        valid = 0
        for row in s.split('\n'):
            pos, char, passw = row.split()
            pos1, pos2 = map(int, pos.split('-'))
            hyp1 = passw[pos1 - 1] == char[0]
            hyp2 = passw[pos2 - 1] == char[0]
            if hyp1 ^ hyp2:
                valid += 1
        return valid
