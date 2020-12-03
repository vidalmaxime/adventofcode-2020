from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        lines = s.split('\n')
        n_pos = len(lines[0])
        count = 0
        for i in range(1, len(lines)):
            pos = (i*3) % n_pos
            if lines[i][pos] == '#':
                count += 1
        return count
