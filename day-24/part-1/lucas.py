from tool.runners.python import SubmissionPy
import re

# https://github.com/matus-pikuliak/advent_2020/blob/master/24/01.py

class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        tiles = dict()
        for line in s.splitlines():
            t = 0j
            for dir in re.findall(r'([ns]?[we])', line):
                t += {'e': 1j, 'w': -1j, 'ne': 1j - 1, 'nw': -1, 'se': 1, 'sw': -1j + 1}[dir]
            tiles[t] = not tiles.get(t, False)
        
        return sum(tiles.values())
