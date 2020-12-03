from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        rows = s.split('\n')
        width = len(rows[0])
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees = [0] * len(slopes)
        for i, row in enumerate(rows[1:], start=1):
            for j, (r, d) in enumerate(slopes):
                if i % d == 0:
                    pos = (i // d * r) % width
                    trees[j] += row[pos] == '#'
        prod = 1
        for tree in trees:
            prod *= tree
        return prod
