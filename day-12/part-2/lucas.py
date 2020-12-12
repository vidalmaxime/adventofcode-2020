from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        instrs = s.split()
        ship_pos = [0,0]
        waypoint = [10,1]
        for inst in instrs:
            action, val = inst[0], int(inst[1:])
            if action == 'F':
                ship_pos[0] += waypoint[0] * val
                ship_pos[1] += waypoint[1] * val
            elif action == 'N':
                waypoint[1] += val
            elif action == 'E':
                waypoint[0] += val
            elif action == 'S':
                waypoint[1] -= val
            elif action == 'W':
                waypoint[0] -= val
            elif action == 'R':
                if val == 90:
                    waypoint = [waypoint[1], waypoint[0]*-1]
                elif val == 180:
                    waypoint = [waypoint[0]*-1, waypoint[1]*-1]
                elif val == 270:
                    waypoint = [waypoint[1]*-1, waypoint[0]]
            elif action == 'L':
                if val == 90:
                    waypoint = [waypoint[1]*-1, waypoint[0]]
                elif val == 180:
                    waypoint = [waypoint[0]*-1, waypoint[1]*-1]
                elif val == 270:
                    waypoint = [waypoint[1], waypoint[0]*-1]
        return abs(ship_pos[0]) + abs(ship_pos[1])
