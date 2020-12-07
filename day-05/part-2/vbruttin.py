from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        occupied_seats = [
            int(seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
            for seat in s.split('\n')
        ]
        occupied_seats.sort()
        for s1, s2 in zip(occupied_seats[:-1], occupied_seats[1:]):
            if s2 - s1 == 2:
                return s1 + 1
