from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        return max(
            int(seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
            for seat in s.split('\n'))
