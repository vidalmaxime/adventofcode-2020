from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        binaries = map(lambda x: x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),
                       s.split('\n'))
        sIds = sorted(map(lambda x:int(x[:-3],2)*8 + int(x[-3:],2), binaries))
        for x,y in zip(sIds, sIds[1:]):
            if y-x > 1:
                return x+1
        return -1
