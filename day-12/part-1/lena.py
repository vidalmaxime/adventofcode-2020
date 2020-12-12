from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        posx = 0
        posy = 0
        dirs = ["E", "S", "W", "N"]
        ptr = 0
        for line in s.split('\n'):
            action, value = line[0], int(line[1:])
            if   action == "N": posy += value
            elif action == "S": posy -= value
            elif action == "E": posx += value
            elif action == "W": posx -= value
            elif action == "L": ptr = (ptr - value // 90) % len(dirs)
            elif action == "R": ptr = (ptr + value// 90) % len(dirs)
            elif action == "F":
                if   dirs[ptr] == "N": posy += value
                elif dirs[ptr] == "S": posy -= value
                elif dirs[ptr] == "E": posx += value
                elif dirs[ptr] == "W": posx -= value
                
        return(abs(posx)+abs(posy))