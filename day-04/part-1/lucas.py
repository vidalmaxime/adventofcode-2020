from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        val_fields = set(fields[:-1])
        passports = s.split('\n\n')
        p_fields = [passport.split(':') for passport in passports]
        count = 0
        for p in p_fields:
            f = [p[i][-3:] for i in range(len(p)-1)]
            if 'cid' in f:
                f.remove('cid')
            f = set(f)
            if f == val_fields:
                count += 1
        return count
