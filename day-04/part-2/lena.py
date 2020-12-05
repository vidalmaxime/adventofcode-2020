from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        passports = s.split("\n\n")
        needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        counter = 0
        for passport in passports:
        	fields = passport.split()
        	v  = 0
        	for field in fields:
        		[pos1, pos2] = field.split(":")
        		if (pos1 =='byr') and (pos2.isdigit()) and (len(pos2) ==4) and (1920<=int(pos2)<=2002):
        			v+=1
        		if (pos1 =='iyr') and (pos2.isdigit()) and (len(pos2) ==4) and (2010<=int(pos2)<=2020):
        			v+=1
        		if (pos1 =='eyr') and (pos2.isdigit()) and (len(pos2) ==4) and (2020<=int(pos2)<=2030):
        			v+=1
        		if (pos1 == 'hgt'):
        			if (pos2.endswith('cm') and (pos2[:-2].isdigit()) and 150<=int(pos2[:-2])<=193):
        				v+=1
        			if (pos2.endswith('in') and (pos2[:-2].isdigit()) and 59<=int(pos2[:-2])<=76):
        				v+=1
        		if (pos1 == 'hcl') and (pos2[0]=='#') and (pos2[1:].isalnum()) and (len(pos2)==7):
        			v+=1
        		if (pos1 == 'ecl') and (pos2 in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        			v+=1
        		if (pos1 == 'pid') and (len(pos2)==9) and (pos2.isdigit()):
        			v+=1
        	if v == len(needed):
        		counter+=1
        return counter
