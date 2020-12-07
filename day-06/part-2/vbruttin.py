from tool.runners.python import SubmissionPy
import string


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        alphabet = set(string.ascii_lowercase)
        total = 0
        for questions in s.split('\n\n'):
            current = alphabet
            for individual in questions.split('\n'):
                current = current.intersection(set(individual))
            total += len(current)
        return total
