from tool.runners.python import SubmissionPy
import re


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        data = [line.replace(' ', '') for line in s.split('\n')]
        return sum(self.evaluate(expr) for expr in data)
        

    def evaluate(self, expr):
        while '(' in expr:
            expr = re.sub(r'\(([^()]+)\)',
                          lambda m: str(self.evaluate(m.group(1))), expr)
        while '+' in expr or '*' in expr:
            expr = re.sub(r'^(\d+)\+(\d+)',
                          lambda m: str(int(m.group(1)) + int(m.group(2))), expr)
            expr = re.sub(r'^(\d+)\*(\d+)',
                          lambda m: str(int(m.group(1)) * int(m.group(2))), expr)
        return int(expr)
