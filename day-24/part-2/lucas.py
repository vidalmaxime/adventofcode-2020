from tool.runners.python import SubmissionPy
import re

# https://github.com/matus-pikuliak/advent_2020/blob/master/24/02.py

class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        tiles = dict()
        for line in s.splitlines():
            t = 0j
            for dir in re.findall(r'([ns]?[we])', line):
                t += {'e': 1j, 'w': -1j, 'ne': 1j - 1, 'nw': -1, 'se': 1, 'sw': -1j + 1}[dir]
            tiles[t] = not tiles.get(t, False)
        black = set(k for k, v in tiles.items() if v)
        
        def neighbours(point):
            return set(point + dif for dif in [1j, -1j, 1j - 1, -1, 1, -1j + 1])
        
        for _ in range(100):
            black = set(p for p in set.union(*[neighbours(b) for b in black])
                if (an := len(black & neighbours(p))) == 2 or p in black and an == 1)
        
        return len(black)
