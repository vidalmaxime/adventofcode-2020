from tool.runners.python import SubmissionPy


class MaximeSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split("\n\n")
        hex = set("0123456789abcdef")
        colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        numbers = set("0123456789")
        big_count = 0
        for passport in lines:
            fields = passport.split()
            keys = set()
            count = 0
            for field in fields:
                key, value = field.split(":")
                keys.add(key)
                if key == "byr" and (int(value) < 1920 or int(value) > 2002):
                    break
                if key == "iyr" and (int(value) < 2010 or int(value) > 2020):
                    break
                if key == "eyr" and (int(value) < 2020 or int(value) > 2030):
                    break
                if key == "hgt":
                    if value.endswith("cm"):
                        if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                            break
                    elif value.endswith("in"):
                        if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                            break
                    else:
                        break
                if key == "hcl":
                    if (not value.startswith("#")) or len(value) != 7:
                        break
                    if any(c not in hex for c in value[1:]):
                        break
                if key == "ecl" and value not in colors:
                    break
                if key == "pid":
                    if len(value) != 9:
                        break
                    if any(c not in numbers for c in value):
                        break
                if key != "cid":
                    count += 1
            if count == 7:
                big_count += 1
        return big_count
