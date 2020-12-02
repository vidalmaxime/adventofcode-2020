from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        s = s.split('\n')
        count = 0
        for line in s:
            pol, letter, pw = line.split(' ')
            low_lim, high_lim = pol.split('-')
            if pw.count(letter[0]) >= int(low_lim) and pw.count(letter[0]) <= int(high_lim):
                count += 1
        return count
