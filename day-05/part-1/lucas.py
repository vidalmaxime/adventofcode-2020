from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        binaries = map(lambda x: x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),
                       s.split('\n'))
        return max(map(lambda x:int(x[:-3],2)*8 + int(x[-3:],2), binaries))
