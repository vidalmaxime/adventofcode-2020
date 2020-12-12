from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        instrs = s.split()
        ship_pos = [0,0]
        ship_dir = 0 # 0=E, 1=S, 2=W, 3=N
        for inst in instrs:
            action, val = inst[0], int(inst[1:])
            if action == 'N' or (action=='F' and ship_dir==3):
                ship_pos[1] += val
            elif action == 'E' or (action=='F' and ship_dir==0):
                ship_pos[0] += val
            elif action == 'S' or (action=='F' and ship_dir==1):
                ship_pos[1] -= val
            elif action == 'W' or (action=='F' and ship_dir==2):
                ship_pos[0] -= val
            elif action == "L":
                ship_dir = (ship_dir - val // 90) % 4
            elif action == "R":
                ship_dir = (ship_dir + val // 90) % 4
        return abs(ship_pos[0]) + abs(ship_pos[1])
