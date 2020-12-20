from tool.runners.python import SubmissionPy
from itertools import product
from math import prod

# taken from https://github.com/matus-pikuliak/advent_2020


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        lines = s.splitlines()
        tiles = {int(lines[i][5:9]): lines[i+1:i+11] for i in range(0, len(lines), 12)}
        
        return prod(i for i in tiles if sum(match(tiles[i], tiles[j]) for j in tiles) == 3)
    

def borders(tile):
    yield tile[0]
    yield tile[-1]
    yield ''.join(line[0] for line in tile)
    yield ''.join(line[-1] for line in tile)


def match(tile1, tile2):
    return any(b1 == b2 or b1 == b2[::-1] for b1, b2 in product(borders(tile1), borders(tile2)))
