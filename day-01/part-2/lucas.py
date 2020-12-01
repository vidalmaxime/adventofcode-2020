from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        entries = sorted(list(map(int,s.split())))
        for k in range(len(entries)):
            i = 0
            j = len(entries)-1
            while i < j:
                sum = entries[i] + entries[j] + entries[k]
                if sum == 2020:
                    return entries[i] * entries[j] * entries[k]
                elif sum > 2020:
                    j -= 1
                else:
                    i += 1
