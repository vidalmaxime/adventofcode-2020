from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        s = s.split()
        time = int(s[0])
        ids = s[1].replace('x,', '')
        buses = [int(i) for i in ids.split(',')]
        wait = max(buses)
        for id_ in buses:
            if id_ - (time % id_) < wait:
                wait = id_ - (time % id_)
                res = wait * id_
        return res


        