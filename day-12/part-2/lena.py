from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        wpx = 10
        wpy = 1
        posx = 0
        posy = 0

        for line in s.split('\n'):
            action, value = line[0], int(line[1:])
            if   action == "N": wpy += value
            elif action == "S": wpy -= value
            elif action == "E": wpx += value
            elif action == "W": wpx -= value
            elif action in ("R", "L") and value== 180:
                wpx, wpy = -wpx, -wpy
            elif action == "R":
                if value== 90:    wpx, wpy =  wpy, -wpx
                elif value== 270: wpx, wpy = -wpy,  wpx
            elif action == "L":
                if value== 90:    wpx, wpy = -wpy,  wpx
                elif value== 270: wpx, wpy =  wpy, -wpx
            elif action == "F":
                posx += value* wpx
                posy += value* wpy
            
        return(abs(posx)+abs(posy))