from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        List = s.split("\n")
        counter = 0
        for l in List:
        	pos, letter, pw = l.split()
        	pos.split("-")
        	l1  = pw[int(pos1)-1]
        	l2 = pw[int(pos2)-1]
        	if (l1 == letter[0] and l2 != letter [0]) or (l1 != letter[0] and l2 == letter [0]):
        		counter += 1

        return counter
