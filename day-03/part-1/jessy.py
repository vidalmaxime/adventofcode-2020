from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        rows = s.split('\n')
        width = len(rows[0])
        pos = 0
        trees = 0
        for row in rows[1:]:
            pos = (pos + 3) % width
            if row[pos] == '#':
                trees += 1
        return trees
