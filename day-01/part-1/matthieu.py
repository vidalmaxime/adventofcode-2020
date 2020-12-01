from tool.runners.python import SubmissionPy


class MatthieuSubmission(SubmissionPy):

    def run(self, s):
        elfs = list(map(int,s.split()))
        elfs = set(elfs)
        for elf in elfs:
            q = 2020-elf
            if q in elfs:
                return q*elf
