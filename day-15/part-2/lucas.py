from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        data = [int(x) for x in s.split(',')]
        numbers = dict()
        numbers = {**numbers, **{data[i]: [i + 1] for i in range(len(data))}}
        last = data[-1]
        for i in range(len(data) + 1, 30000000 + 1):
            if len(numbers[last]) > 1:
                last = numbers[last][-1] - numbers[last][-2]
            else:
                last = 0
            if last in numbers.keys():
                numbers[last].append(i)
            else:
                numbers[last] = [i]
        return last
        