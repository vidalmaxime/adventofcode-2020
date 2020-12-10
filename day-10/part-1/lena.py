from tool.runners.python import SubmissionPy
from numpy import array, diff

class LenaSubmission(SubmissionPy):

    def run(self, s):
        s = list(sorted(map(int,s.split('\n'))))
        s = [0]+s+[max(s)+3]
        d = array(diff(s))
        return(sum(d ==1)*sum(d==3))
