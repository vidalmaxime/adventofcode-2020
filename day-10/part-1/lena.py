from tool.runners.python import SubmissionPy

class LenaSubmission(SubmissionPy):

    def run(self, s):
        s = list(sorted(map(int,s.split('\n'))))
        s = [0]+s+[max(s)+3]
        #d = list([s[i+1]-s[i] for i in range(len(s)-1)])
        ones = 0
        threes = 0
        for low, high in zip(s, s[1:]):
            if high - low == 3:
                threes += 1
            elif high - low == 1:
                ones += 1
        return ones*threes
