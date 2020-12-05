from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        max_id = 0
        for seat in s.split('\n'):
            row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
            column = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
            max_id = max(max_id, row * 8 + column)
        return max_id
