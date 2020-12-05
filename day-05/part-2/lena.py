from tool.runners.python import SubmissionPy
import numpy as np

class LenaSubmission(SubmissionPy):
    

    def run(self, s):
        seats = s.split()
        numbers = []
        for seat in seats:
            binary = seat.replace('F','0').replace('B', '1').replace('L','0').replace('R', '1')
            numbers.append(int(binary[:-3],2)*8 + int(binary[-3:],2))
            missing = set(range(min(numbers), max(numbers)))-set(numbers)
        return list(missing)[0]

    