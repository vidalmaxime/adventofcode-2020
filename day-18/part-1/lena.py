from tool.runners.python import SubmissionPy
import re

class LenaSubmission(SubmissionPy):

    def run(self, s):
        sum_ = 0
        for l in s.split('\n'):
            l = re.sub(r'(\d+)' , r'p1(\1)', l)
            l = l.replace('*' , '-')
            sum_ += eval(l).val

        return(sum_)

class p1:
    def __init__(self,val):
        self.val = val

    def __add__(self,other):
        return p1(self.val + other.val)

    def __sub__(self,other):
        return p1(self.val * other.val)

        '''
        sum_ = 0
        lines = s.split('\n')
        for line in lines:
            line = line.replace(' ','')
            while re.findall(r'(\([\d+*]+\))' , line):
                grp = re.findall(r'(\([\d+*]+\))' , line)
                for par in grp:
                    line = line.replace(par, evaluate(par[1:-1]))
            sum_ += int(evaluate(line))
        return sum

def evaluate(input_):
    while '*' in input_ or '+' in input_:
        group = re.findall(r'\d+[+*]\d+', input_)
        inp = input_.replace(group[0] , str(eval(group[0])) , 1)
    return inp
    '''