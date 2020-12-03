from tool.runners.python import SubmissionPy

class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n")
        trees_product = 1
        directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        height = len(lines)
        width = len(lines[0])
        for direction in directions:
            trees = 0
            r = direction[0]
            d = direction[1]
            while d < height:
                if lines[d][r] == '#':
                    trees += 1
                r = (r + direction[0]) % width
                d = d + direction[1]
            trees_product *= trees
        return trees_product
