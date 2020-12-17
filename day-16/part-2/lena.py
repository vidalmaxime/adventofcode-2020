from tool.runners.python import SubmissionPy
import copy

class LenaSubmission(SubmissionPy):
    '''
    part two doesn't work and i cannot find the part where things go wrong... so this is done using lucas' part 2
    '''
    def run(self, s):
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
        '''
        rule_data, me, ticket_data = [x.split('\n') for x in s.split('\n\n')]
        my_ticket = [int(x) for x in me[1].split(',')]
        restrictions = {}
        for line in rule_data:
            field, rules = line.split(': ')
            rules = rules.split(' or ')
            rules = [rule.split('-') for rule in rules]
            restrictions[field] = [[int(num) for num in rule] for rule in rules]
            # { 'departure location' : [[49, 920], [932, 950]] }

        tickets = []
        ticket_data = [line.split(',') for line in ticket_data]
        for line in ticket_data:
            tickets.append([int(num) for num in line if num.isnumeric()])
            # [[337, 687, 607, ...], [896, 791, 715, ...], [...]]

        # Use: restrictions, my_ticket, tickets
        forbidden_numbers = set()
        lower_bound = min(restrictions[r][0][0] for r in restrictions)
        upper_bound = max(restrictions[r][1][1] for r in restrictions)
        mid_l_bound = max(restrictions[r][0][1] for r in restrictions)
        mid_u_bound = min(restrictions[r][1][0] for r in restrictions)
        for r in restrictions:
            for i in range(mid_l_bound+1, mid_u_bound-1):
                forbidden_numbers.add(i)

        invalid_values = []
        for ticket in tickets:
            for num in ticket:
                if num in forbidden_numbers or num < lower_bound or num > upper_bound:
                    invalid_values.append(num)
                    
            valid_tickets = []
            for ticket in tickets:
                is_valid = True
                for num in ticket:
                    if num in invalid_values:
                        is_valid = False
                        break
                if is_valid:
                    valid_tickets.append(ticket)

        # fields holds a list of list
        fields = []
        for i in range(len(tickets[0])):
            fields.append([tickets[i] for ticket in valid_tickets])

        # remaining restrictions
        r_res = copy.deepcopy(restrictions)
        correct_field = {}
        for f in fields:
            for r in r_res:
                l_b = r_res[r][0][0]
                mlb = r_res[r][0][1]
                mub = r_res[r][1][0]
                u_b = r_res[r][1][1]

                if all((l_b <= n <= mlb or mub <= n <= u_b) for n in f):
                    correct_field.setdefault(r, []).append(fields.index(f))

        # c_f is correct_fields but with only 1 value
        c_f = dict()
        for f1 in correct_field:
            for f2 in correct_field:
                chk = set(correct_field[f1]).difference(set(correct_field[f2]))
                if len(chk) == 1:
                    c_f[f1] = chk.pop()

        # Multiply the 6 departure values together
        total = 1
        for f in c_f:
            if 'departure' in f:
                total *= my_ticket[c_f[f]]

        return(total)  #5977293343129
        '''

