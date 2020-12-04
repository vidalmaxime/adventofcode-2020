from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        valid = 0
        for passport in s.split('\n\n'):
            if all(req_field in passport for req_field in req_fields):
                valid += 1
        return valid

