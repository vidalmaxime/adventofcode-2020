from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        adapters = sorted(list(map(int, s.split('\n'))) + [0])
        counter = [0, 0, 0, 1]    # add 1 for device
        for a, b in zip(adapters[:-1], adapters[1:]):
            counter[b - a] += 1
        return counter[1] * counter[3]
