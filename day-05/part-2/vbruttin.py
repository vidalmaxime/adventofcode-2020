from tool.runners.python import SubmissionPy
import numpy as np


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        occupied_seats = []
        for seat in s.split('\n'):
            row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
            column = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
            occupied_seats.append(row * 8 + column)
        occupied_seats = np.sort(np.array(occupied_seats))
        missing_index = np.argmax(np.diff(occupied_seats))
        return occupied_seats[missing_index] + 1
