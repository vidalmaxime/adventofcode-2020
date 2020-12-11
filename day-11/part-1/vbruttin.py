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
        for i in [row - 1, row, row + 1]:
            for j in [column - 1, column, column + 1]:
                if (i < 0 or i >= self.rows) or (j < 0 or j >= self.columns) or (i == row and j == column):
                    continue
                total += layout[i, j]
        if total <= 8:
            return 10
        elif total >= 40:
            return 1
        else:
            return layout[row, column]
