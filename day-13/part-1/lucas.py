from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        s = s.split()
        timestamp = int(s[0])
        busIds = [int(i) for i in s[1].replace('x,', '').split(',')]
        wait = max(busIds)
        for id_ in busIds:
            if id_ - (timestamp % id_) < wait:
                wait = id_ - (timestamp % id_)
                res = wait * id_
        return res
    