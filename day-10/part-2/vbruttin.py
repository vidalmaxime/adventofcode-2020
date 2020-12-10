# from tool.runners.python import SubmissionPy
from tool.runners.python import SubmissionPy
from math import prod


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        self.numbers = {1: 1, 2: 2, 3: 4}    # seed of the sequence
        adapters = sorted(list(map(int, s.split('\n'))) + [0])
        groups = []
        count = 0
        for a, b in zip(adapters[:-1], adapters[1:]):
            if b - a == 1:
                count += 1
            elif b - a == 3:
                if count:
                    groups.append(count)
                    count = 0
            else:
                raise NotImplementedError('unexpected 2 gap')
        # Add last group if it does not end with a 3 gap
        if count:
            groups.append(count)

        # Get valid combinations for each group and return the product
        return prod([self.get_tribonnaci(x) for x in groups])

    def get_tribonnaci(self, n):
        """
        Return nth value of the modified Tribonnaci sequence
        Expand the sequence if necessary
        """
        if n not in self.numbers:
            current_n = max(self.numbers)
            while current_n < n:
                current_n += 1
                self.numbers[current_n] = self.numbers[current_n - 1] + \
                                          self.numbers[current_n - 2] + \
                                          self.numbers[current_n - 3]
        return self.numbers[n]


### Script below is to get a feel of the sequence
# Then search on http://oeis.org/ to find which sequence it is --> A000073 Tribonnaci numbers
# Finally implement a function that dynamically updates the sequence --> get_tribonnaci

# from itertools import chain, combinations

# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1))

# counts = []

# for n in range(1, 25):
#     s = [0] + list(range(1, n + 1))
#     max_ = max(s) + 3
#     s = s + [max_]
#     count = 0
#     for subset in powerset(s):
#         if subset and subset[0] == 0 and subset[-1] == max_:
#             for a, b in zip(subset[:-1], subset[1:]):
#                 if b - a > 3:
#                     break
#             else:
#                 count += 1
#     counts.append(count)
# print(counts)