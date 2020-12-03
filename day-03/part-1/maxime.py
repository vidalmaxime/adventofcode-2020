from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.split('\n')
        r = 3
        width = len(lines[0])
        trees = 0
        for line in lines[1:]:
            if line[r] == '#':
                trees += 1
            r = (r + 3) % width
        return trees
