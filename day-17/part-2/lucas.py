from tool.runners.python import SubmissionPy
from itertools import product
from operator import add


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        data = [list(line) for line in s.split('\n')]
        

        deltas = list(product((-1, 0, 1), repeat=4))
        cells = {}
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == '#':
                    coord = (i, j) + (0,) * (4 - 2)
                    cells[coord] = 1
    
        for i in range(6):
            temp = {}
            for coord in cells.keys():
                n = sum(cells.get(tuple(map(add, coord, delta)), 0) for delta in deltas)
                if n == 3 or n == 4:
                    temp[coord] = 1
    
                for neighbour in deltas:
                    neighbour = tuple(map(add, coord, neighbour))
                    if neighbour not in cells:
                        n = sum(cells.get(tuple(map(add, neighbour, delta)), 0) for delta in deltas)
                        if n == 3:
                            temp[neighbour] = 1
            cells = temp
            
        return len(cells)
        