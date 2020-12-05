from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n\n")
        fields = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "hcl"]
        big_count = 0
        for line in lines:
            count = sum(1 for field in fields if field in line)
            if count == len(fields):
                big_count += 1

        return big_count
