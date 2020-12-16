from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        rules, _, nearby = [x.split('\n') for x in s.split('\n\n')]
        
        rules = [rule.split(': ')[1].split(' or ') for rule in rules]
        rules_ = dict()
        for i, r in enumerate(rules):
            range1, range2 = [i.split('-') for i in r]
            rules_[i] = [int(range1[0]), int(range1[1]), int(range2[0]), int(range2[1])]
        
        nearby = nearby[1:]
        res = 0
        for ticket in nearby:
            nums = [int(x) for x in ticket.split(',')]        
            for num in nums:
                cnt = 0
                for rule in rules_.values():
                    if not(num>=rule[0] and num<=rule[1]) and not(num>=rule[2] and num<=rule[3]):
                        cnt += 1
                if cnt == len(rules_):
                    res += num
    
        return res
    