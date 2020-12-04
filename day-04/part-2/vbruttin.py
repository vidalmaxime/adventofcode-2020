from tool.runners.python import SubmissionPy
import re


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        mandatory_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        counter = 0
        for passport in s.split('\n\n'):
            if not (mandatory_fields - set(re.findall(r'\w+(?=:)', passport))):
                for field in re.split(r'\n|\s+', passport):
                    category = field[:3]
                    if category == 'byr':
                        value = field[4:]
                        if value.isdigit() and 1920 <= int(value) <= 2002:
                            continue
                        else:
                            break
                    elif category == 'iyr':
                        value = field[4:]
                        if value.isdigit() and 2010 <= int(value) <= 2020:
                            continue
                        else:
                            break
                    elif category == 'eyr':
                        value = field[4:]
                        if value.isdigit() and 2020 <= int(value) <= 2030:
                            continue
                        else:
                            break
                    elif category == 'hgt':
                        unit = field[-2:]
                        if unit == 'cm':
                            value = field[4:-2]
                            if value.isdigit() and 150 <= int(value) <= 193:
                                continue
                            else:
                                break
                        elif unit == 'in':
                            value = field[4:-2]
                            if value.isdigit() and 59 <= int(value) <= 76:
                                continue
                            else:
                                break
                        else:
                            break
                    elif category == 'hcl':
                        value = field[5:]
                        if field[4] == '#' and re.match(r'([0-9]|[a-f]){6}$', value):
                            continue
                        else:
                            break
                    elif category == 'ecl':
                        if field[4:] in colors:
                            continue
                        else:
                            break
                    elif category == 'pid':
                        value = field[4:]
                        if value.isdigit() and len(value) == 9:
                            continue
                        else:
                            break
                    elif category == 'cid':
                        continue
                    else:
                        break
                else:
                    counter += 1
        return counter
