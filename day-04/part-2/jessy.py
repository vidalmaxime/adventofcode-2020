import re
from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        r = re.compile('(\w{3}):([^\s]+)')
        valid = 0
        for passport in s.split('\n\n'):
            fields = dict(r.findall(passport))
            if any(req_field not in fields for req_field in req_fields):
                continue

            hgt = fields['hgt']
            if hgt.endswith('cm'):
                cond4 = 150 <= int(hgt[:-2]) <= 193
            elif hgt.endswith('in'):
                cond4 = 59 <= int(hgt[:-2]) <= 76
            else:
                continue

            hcl = fields['hcl']
            if hcl.startswith('#') and len(hcl) == 7:
                cond5 = all('a' <= char <= 'f' for char in hcl[1:] if char.isalpha())
            else:
                continue

            cond1 = 1920 <= int(fields['byr']) <= 2002
            cond2 = 2010 <= int(fields['iyr']) <= 2020
            cond3 = 2020 <= int(fields['eyr']) <= 2030
            cond6 = fields['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
            cond7 = len(fields['pid']) == 9
            if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7:
                valid += 1
        return valid
