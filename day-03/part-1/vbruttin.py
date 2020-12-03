from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        lines = s.split('\n')
        length = len(lines[0])

        return sum(1 for location, line in enumerate(lines) if line[(3 * location) % length] == '#')
