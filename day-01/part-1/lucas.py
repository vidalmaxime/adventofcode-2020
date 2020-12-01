from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        entries = sorted(list(map(int,s.split())))
        i = 0
        j = len(entries)-1
        while True:
            sum = entries[i] + entries[j]
            if sum == 2020:
                return entries[i] * entries[j]
            elif sum > 2020:
                j -= 1
            else:
                i += 1