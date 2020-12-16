from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        rules, mine, nearby = [x.split('\n') for x in s.split('\n\n')]
        mine = [int(x) for x in mine[1].split(',')]
        
        rule_names = [rule.split(': ')[0] for rule in rules]
        rules = [rule.split(': ')[1].split(' or ') for rule in rules]
        rules_ = dict()
        for i, r in enumerate(rules):
            range1, range2 = [i.split('-') for i in r]
            rules_[i] = [int(range1[0]), int(range1[1]), int(range2[0]), int(range2[1])]
        
        # throwing out invalid tickets
        nearby = nearby[1:]
        invalid = []
        for i, ticket in enumerate(nearby):
            nums = [int(x) for x in ticket.split(',')]        
            for num in nums:
                cnt = 0
                for rule in rules_.values():
                    if not(num>=rule[0] and num<=rule[1]) and not(num>=rule[2] and num<=rule[3]):
                        cnt += 1
                if cnt == len(rules_):
                    invalid.append(i)
                    break
        invalid = sorted(invalid, reverse=True)
        for i in invalid:
            nearby.pop(i)
        
        # searching for valid fields
        not_valid = {field: [] for field in rule_names}
        for ticket in nearby:
            nums = [int(x) for x in ticket.split(',')]
            for i, num in enumerate(nums):
                for j, rule in enumerate(rules_.values()):
                    if not(num>=rule[0] and num<=rule[1]) and not(num>=rule[2] and num<=rule[3]):
                        not_valid[rule_names[j]].append(i)
        
        valid = not_valid.copy()
        for key, val in not_valid.items():
            valid[key] = [i for i in range(len(mine)) if i not in val]
        
        matching = dict()
        for i in range(1, len(mine)+1):
            for k,v in valid.items():
                if len(v) == i:
                    for el in v:
                        if not el in matching.values():
                            matching[k] = el
        
        res = 1
        for field in matching:
            if field.startswith('departure'):
                res *= mine[matching[field]]
            
        return res
    