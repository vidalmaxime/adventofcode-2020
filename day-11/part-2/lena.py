from tool.runners.python import SubmissionPy
import copy

class LenaSubmission(SubmissionPy):

    def run(self, s):
        grid =  [list(i) for i in s.split('\n')]
        new_grid = copy.deepcopy(grid)
        while True:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    #print("p", grid[y][x])
                    if grid[y][x] != ".":
                        counter = get_first_seat(grid, (x,y))

                        #print("c", counter)
                        if grid[y][x] == "#" and counter >= 5:
                            new_grid[y][x] = "L"
                        elif grid[y][x] == "L" and counter == 0:
                            new_grid[y][x] = "#"
            if new_grid == grid:
                p2 = 0
                for i in new_grid:
                    p2 += i.count("#")
                return p2
            grid = copy.deepcopy(new_grid)
def get_first_seat(grid, point):
    x, y = point
    count_list = []

    x_val = x +1
    y_val = y
    #right
    while 0 <= x_val <= len(grid[0]) - 1:
        if grid[y][x_val] in ["L","#"]:
            if grid[y][x_val] == "L":
                break
            elif grid[y][x_val] == "#":
                count_list.append(1)
                break
        x_val += 1

    x_val = x - 1
    y_val = y
    #left
    while 0 <= x_val <= len(grid[0]) - 1:
        if grid[y][x_val] in ["L","#"]:
            if grid[y][x_val] == "L":
                break
            elif grid[y][x_val] == "#":
                count_list.append(1)
                break
        x_val -= 1

    x_val = x
    y_val = y - 1
    #up
    while 0 <= y_val <= len(grid) -1 and 0 <= x <= len(grid[0]) - 1:
        if grid[y_val][x] in ["L","#"]:
            if grid[y_val][x] == "L":
                break
            elif grid[y_val][x] == "#":
                count_list.append(1)
                break
        y_val -= 1

    x_val = x
    y_val = y + 1
    #down
    while 0 <= y_val <= len(grid) -1 and 0 <= x <= len(grid[0]) - 1:
        if grid[y_val][x] in ["L","#"]:
            if grid[y_val][x] == "L":
                break
            elif grid[y_val][x] == "#":
                count_list.append(1)
                break
        y_val += 1

    #leftdown
    x_val = x - 1
    y_val = y + 1
    while 0 <= y_val <= len(grid) -1 and 0 <= x_val <= len(grid[0]) - 1:
        if grid[y_val][x_val] in ["L","#"]:
            if grid[y_val][x_val] == "L":
                break
            elif grid[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val += 1
        x_val -= 1


    #rightdown
    x_val = x + 1
    y_val = y + 1
    while 0 <= y_val <= len(grid) -1 and 0 <= x_val <= len(grid[0]) - 1:
        if grid[y_val][x_val] in ["L","#"]:
            if grid[y_val][x_val] == "L":
                break
            elif grid[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val += 1
        x_val += 1

    #rightup
    x_val = x + 1
    y_val = y - 1
    while 0 <= y_val <= len(grid) -1 and 0 <= x_val <= len(grid[0]) - 1:
        if grid[y_val][x_val] in ["L","#"]:
            if grid[y_val][x_val] == "L":
                break
            elif grid[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val -= 1
        x_val += 1

    #leftup
    x_val = x - 1
    y_val = y - 1
    while 0 <= y_val <= len(grid) - 1 and 0 <= x_val <= len(grid[0]) - 1:
        if grid[y_val][x_val] in ["L", "#"]:
            if grid[y_val][x_val] == "L":
                break
            elif grid[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val -= 1
        x_val -= 1
    return sum(count_list)
