from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        passports = s.split("\n\n")
        needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        counter = 0
        for passport in passports:
        	valid = True
        	fields = passport.split()
        	v  = 0
        	for field in fields:
        		[pos1, pos2] = field.split(":")
        		if pos1 in needed:
        			v+=1

        	if v == len(needed):
        		counter+=1
        return counter