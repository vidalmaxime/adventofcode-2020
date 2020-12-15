from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        start = list(map(int, s.split(',')))
        previous = {x: i + 1 for i, x in enumerate(start)}
        last = start[-1]
        for i in range(len(start)+1, 30000001):
            current = i -1 - previous[last] if last in previous else 0
            previous[last] = i-1
            last = current
        return last