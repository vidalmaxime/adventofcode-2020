from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        trans = str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'})
        ids = set(int(seat.translate(trans), 2) for seat in s.split('\n'))
        return (set(range(min(ids), max(ids) + 1)) - ids).pop()
