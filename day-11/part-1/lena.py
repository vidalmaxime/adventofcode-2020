from tool.runners.python import SubmissionPy
import copy

class LenaSubmission(SubmissionPy):

    def run(self, s):
        seat_map = [list(i) for i in s.split('\n')]
        #seat_map = s.split('\n')
        new_map = copy.deepcopy(seat_map)

        diff = True
        while True:
            #iterate over all the lists. y comes first since we are taking all the rows one by one
            for y in range(len(seat_map)):
                for x in range(len(seat_map[0])):
                    #only do smth if we have a seat
                    if seat_map[y][x] != ".":
                        list_of_points = adj_points((x, y))
                        counter = 0
                        for i in list_of_points:
                            y_val = i[1]
                            x_val = i[0]
                            #if the point being evaluated is in bounds of the grid, check if occupied and if so, count.
                            if 0 <= y_val <= len(seat_map) -1 and 0 <= x_val <= len(seat_map[0]) - 1:
                                if seat_map[y_val][x_val] == "#":
                                    counter += 1
                        #apply the rules to the occupied or empty seat
                        if seat_map[y][x] == "#" and counter >= 4:
                            new_map[y][x] = "L"
                        elif seat_map[y][x] == "L" and counter == 0:
                            new_map[y][x] = "#"
            # if our mutated new_grid is equal to the old, untouched grid, we found the equlibrium!
            if new_map == seat_map:
                p1 = 0
                #iterate over all rows and count the occurence of "#"
                for i in new_map:
                    p1 += i.count("#")
                return (p1)

                #break
            #if we finish the round, our new reference (old) grid will be the current working grid. So we make a deepcopy
            #and use that copy as a reference to check against. It has to be a deepcopy so we also copy the lists in the list.
            seat_map = copy.deepcopy(new_map)

def adj_points(point):
    x, y = point
    return [(x + 1, y), (x - 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x, y + 1), (x, y - 1)]
