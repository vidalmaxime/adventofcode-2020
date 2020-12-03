from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        lines = s.split('\n')
        length = len(lines[0])

        steps = [1, 3, 5, 7]
        product = 1

        for step in steps:
            product *= sum(1 for location, line in enumerate(lines) if line[(step * location) % length] == '#')

        return product * sum(1 for location, line in enumerate(lines[::2]) if line[location % length] == '#')