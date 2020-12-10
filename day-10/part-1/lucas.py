from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        adapters = sorted(list(map(int,s.split())))
        adapters = [0] + adapters + [adapters[-1]+3]
        cnt = {0: 0, 1: 0, 2: 0, 3: 0}
        for i in range(len(adapters)-1):
            cnt[adapters[i+1]-adapters[i]] += 1
        return cnt[1] * cnt[3]
