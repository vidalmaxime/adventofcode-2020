from tool.runners.python import SubmissionPy


directions = [(+1, 0), (-1, 0), (0, +1), (0, -1), (-1, -1), (+1, -1), (+1, +1), (-1, +1)]

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        lines = [line for line in s.split()]
        tolerance_lvl = 5
        care_immediately_adjacent_seats = False
        
        prev_layout = []
        layout = lines.copy()

        while layout != prev_layout:
            prev_layout = layout.copy()
            layout = []
    
            for row_ix, prev_row in enumerate(prev_layout):
                row = ''
    
                for col_ix, prev_position in enumerate(prev_row):
                    if care_immediately_adjacent_seats:
                        num = nr_occupied_immediately_adjacent_seats(prev_layout, row_ix, col_ix)
                    else:
                        num = nr_occupied_first_next_seats(prev_layout, row_ix, col_ix)
    
                    if num == 0 and prev_position == EMPTY_SEAT:
                        row += OCCUPIED_SEAT
                    elif num >= tolerance_lvl and prev_position == OCCUPIED_SEAT:
                        row += EMPTY_SEAT
                    else:
                        row += prev_position
    
                layout.append(row)
        
        return sum([row.count(OCCUPIED_SEAT) for row in layout])    
        

    


def nr_occupied_immediately_adjacent_seats(layout, row_ix, col_ix):
    cnt = 0
    row_len = len(layout)
    col_len = len(layout[row_ix])
    for row_dir, col_dir in directions:
        rix = row_ix + row_dir
        cix = col_ix + col_dir
        if (0 <= rix < row_len) and (0 <= cix < col_len) and (layout[rix][cix] == OCCUPIED_SEAT):
            cnt += 1
    return cnt


def nr_occupied_first_next_seats(layout, row_ix, col_ix):
    cnt = 0
    row_len = len(layout)
    col_len = len(layout[row_ix])
    for row_dir, col_dir in directions:
        rix = row_ix + row_dir
        cix = col_ix + col_dir
        while (0 <= rix < row_len) and (0 <= cix < col_len):
            if layout[rix][cix] == EMPTY_SEAT:
                break
            if layout[rix][cix] == OCCUPIED_SEAT:
                cnt += 1
                break
            rix += row_dir
            cix += col_dir
    return cnt

