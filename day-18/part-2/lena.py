from tool.runners.python import SubmissionPy
import re

class LenaSubmission(SubmissionPy):

    def run(self, s):
        sum_ = 0
        for l in s.split('\n'):
            l = re.sub(r'(\d+)' , r'p2(\1)', l)
            l = l.replace('*' , '-')
            l = l.replace('+' , '*')
            sum_ += eval(l).val

        return(sum_)

class p2:
    def __init__(self,val):
        self.val = val

    def __sub__(self,other):
        return p2(self.val * other.val)

    def __mul__(self,other):
        return p2(self.val + other.val)