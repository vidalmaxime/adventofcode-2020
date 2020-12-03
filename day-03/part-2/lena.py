from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n")
        rights = [1,3,5,7,1]
        downs = [1,1,1,1,2]
        trees = 1
        w = len(lines[0])
        for i in range(len(rights)):
        	counter = 0
        	right = rights[i]
        	down = downs[i]
        	while down < len(lines):
        		if lines[down][right] == '#': #note: first index is for line, second for position in line
        			counter +=1
        		right = (right + rights[i])%w
        		down = (down + downs[i])
        	trees *= counter
        return trees
