from tool.runners.python import SubmissionPy
from itertools import product
from math import prod

# taken from https://github.com/matus-pikuliak/advent_2020


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        lines = s.splitlines()
        self.tiles = [lines[i+1:i+11] for i in range(0, len(lines), 12)]
        
        final = {0j: self.tiles[0]}
        self.tiles.remove(self.tiles[0])
        queue = [0j]
        
        while queue:
            pos = queue.pop()
            for dr in [-1, 1j, 1, -1j]:
                npos = pos + dr
                if npos in final:
                    continue
                if n := self.neighbor(final[pos], dr):
                    final[npos] = n
                    queue.append(npos)
        
        
        min_r = min(int(k.real) for k in final)
        min_i = min(int(k.imag) for k in final)
        sea = [
            final[big_line + big_col * 1j][line][col]
            for big_line in range(min_r, min_r + 12)
            for line in range(1, 9)
            for big_col in range(min_i, min_i + 12)
            for col in range(1, 9) ]
        
        
        def find_monsters(sea, monster):
            return sum(all(sea[pos + j] == '#' for j in monster) for pos in range(len(sea) - max(monster)) if sea[pos] == '#')
        
        lochness = """
                          # 
        #    ##    ##    ###
         #  #  #  #  #  #   
        """
        lr_monster = [78, 83, 84, 89, 90, 95, 96, 97, 175, 178, 181, 184, 187, 190]
        rl_monster = [95, 96, 97, 102, 103, 108, 109, 114, 194, 197, 200, 203, 206, 209]
        
        for _ in range(4):
            for monster in [lr_monster, rl_monster]:
                if m := find_monsters(sea, monster):
                    return sea.count('#') - lochness.count('#') * m
            sea = [ sea[(95 - j) * 96 + i] for i in range(96) for j in range(96) ]
    
        return -1
    
    
    def border(self, tile):
        return {-1: tile[0],
                1j: ''.join(line[-1] for line in tile),
                1: tile[-1][::-1],
                -1j: ''.join(line[0] for line in tile)[::-1]}
    
    def neighbor(self, tile, dr):
        b = self.border(tile)[dr]
        for t in self.tiles:
            ot = t
            if b in self.border(t).values():
                t = t[::-1]
            if b[::-1] in self.border(t).values():
                self.tiles.remove(ot)
                while self.border(t)[-dr][::-1] != b:
                    t = [''.join(t[j][i] for j in range(10))[::-1] for i in range(10)]
                return t
    