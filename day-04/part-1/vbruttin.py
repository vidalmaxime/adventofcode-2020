from tool.runners.python import SubmissionPy
import re


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        mandatory_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        return sum(not (mandatory_fields - set(re.findall(r'\w+(?=:)', passport))) for passport in s.split('\n\n'))
