from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        card_key, door_key = map(int, s.splitlines())
        acc = 1
        loop = 0
        while acc != card_key:
            loop += 1
            acc = acc * 7 % 20201227
        
        return pow(door_key, loop, 20201227)
