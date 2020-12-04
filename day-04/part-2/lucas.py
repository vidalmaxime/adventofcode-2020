from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        val_fields = set(fields[:-1])
        passports = s.split('\n\n')
        p_fields = [passport.replace('\n', ' ').split(' ') for passport in passports]
        count = 0
        for p in p_fields:
            p_dict = { i.split(':')[0] : i.split(':')[1] for i in p }
            if 'cid' in p_dict.keys():
                p_dict.pop('cid')
            if set(p_dict.keys()) == val_fields:
                if len(p_dict['byr'])==4 and int(p_dict['byr'])>=1920 and int(p_dict['byr'])<=2002:
                    if len(p_dict['iyr'])==4 and int(p_dict['iyr'])>=2010 and int(p_dict['iyr'])<=2020:
                        if len(p_dict['eyr'])==4 and int(p_dict['eyr'])>=2020 and int(p_dict['eyr'])<=2030:
                            if (p_dict['hgt'].endswith('cm') and int(p_dict['hgt'][:-2])>=150 and int(p_dict['hgt'][:-2])<=193) \
                                or (p_dict['hgt'].endswith('in') and int(p_dict['hgt'][:-2])>=59 and int(p_dict['hgt'][:-2])<=76):
                                    if p_dict['hcl'].startswith('#') and len(p_dict['hcl'])==7:
                                        if p_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                            if len(p_dict['pid'])==9 and p_dict['pid'].isdigit():
                                                count += 1
                                    
        return count
    