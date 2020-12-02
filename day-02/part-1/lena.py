from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        List = s.split("\n")
        counter = 0
        for l in List:
        	limits, letter, pw = l.split()
        	[lower, upper] = limits.split("-")
        	instances = pw.count(letter[0])
        	if instances >= int(lower) and instances <= int(upper):
        		counter += 1

        return counter
