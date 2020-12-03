from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        lines = s.split("\n")
        right = 3
        counter = 0
        w = len(lines[0])
        for l in lines[1:]:
        	if l[right] == '#':
        		counter +=1
        	right = (right + 3)%w # ever repeating line
        return counter

