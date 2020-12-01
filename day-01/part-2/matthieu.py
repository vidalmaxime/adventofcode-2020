from tool.runners.python import SubmissionPy


class MatthieuSubmission(SubmissionPy):

    def run(self, s):
        elfs_sort = sorted(list(map(int,s.split())))
        elfs = set(elfs_sort)
        for elf1 in elfs:
            for elf2 in elfs_sort:
                if elf2>2020-elf1:
                    break
                q = 2020-elf1-elf2
                if q in elfs:
                    return q*elf1*elf2
