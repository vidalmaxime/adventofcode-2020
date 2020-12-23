from tool.runners.python import SubmissionPy
from array import array

# https://github.com/ephemient/aoc2020/blob/main/py/src/aoc2020/day23.py

class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        arr = array('I', (0, ) * 9)
        nums = [int(c) for c in s if c.isdigit()]
        for i, x in enumerate(nums):
            arr[x - 1] = nums[(i + 1) % len(nums)] - 1
        x = nums[0] - 1
        for _ in range(100):
            x = step(arr, x)
        x, acc = 0, 0
        while True:
            x = arr[x]
            if not x:
                return acc
            acc = 10 * acc + x + 1
        return -1

def step(arr, x):
    a = arr[x]
    b = arr[a]
    c = arr[b]
    y = arr[c]
    t = x
    while True:
        t = t - 1 if t > 0 else len(arr) -1
        if t not in (a, b, c):
            break
    u = arr[t]
    arr[x] = y
    arr[t] = a
    arr[c] = u
    return y
