from tool.runners.python import SubmissionPy
import copy

class LenaSubmission(SubmissionPy):

    def run(self, s):
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

