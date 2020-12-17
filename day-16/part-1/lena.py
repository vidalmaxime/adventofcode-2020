from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        rule_lines, me, ticket_data = [x.split('\n') for x in s.split('\n\n')]
        restrictions = {}
        for line in rule_lines:
            field, rules = line.split(': ')
            rules = rules.split(' or ')
            rules = [rule.split('-') for rule in rules]
            restrictions[field] = [[int(num) for num in rule] for rule in rules]
        tickets = []
        ticket_data = [line.split(',') for line in ticket_data]
        for line in ticket_data:
            tickets.append([int(num) for num in line if num.isnumeric()])
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
                if (num in forbidden_numbers) or (num < lower_bound) or (num > upper_bound):
                    invalid_values.append(num)
                
        ticket_error_rate = sum(invalid_values)
        return(ticket_error_rate) 
