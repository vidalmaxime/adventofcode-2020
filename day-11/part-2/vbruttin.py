from tool.runners.python import SubmissionPy
import numpy as np


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        data = []
        for line in s.split('\n'):
            formatted_line = '[' + ','.join(line) + ']'
            data.append(eval(formatted_line.replace('.', '0').replace('L', '1')))
        layout = np.array(data)
        layout_copy = np.zeros(1)
        self.rows, self.columns = layout.shape
        while not np.array_equal(layout, layout_copy):
            layout_copy = layout.copy()
            for row in range(self.rows):
                for column in range(self.columns):
                    if layout[row, column] == 1:
                        layout[row, column] = self.adjacency(layout_copy, row, column)
                    elif layout[row, column] == 10:
                        layout[row, column] = self.adjacency(layout_copy, row, column)
                    else:
                        continue

        return np.count_nonzero(layout == 10)

    def adjacency(self, layout, row, column):
        total = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                inner_row = row + i
                inner_column = column + j

                if (inner_row < 0 or inner_row >= self.rows) or (inner_column < 0 or inner_column >= self.columns) or (
                        inner_row == row and inner_column == column):
                    continue

                while not layout[inner_row, inner_column]:
                    if (0 <= inner_row + i < self.rows) and (0 <= inner_column + j < self.columns):
                        inner_row += i
                        inner_column += j
                    else:
                        break
                total += layout[inner_row, inner_column]
        if total <= 8:
            return 10
        elif total >= 50:
            return 1
        else:
            return layout[row, column]
