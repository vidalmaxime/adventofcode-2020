from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        numbers = list(map(int,s.split()))
        for i in range(25, len(numbers)):
            if not self.is_sum(numbers[i], numbers[i-25:i]):
                return numbers[i]
            
            
    def is_sum(self, number, numbers):
        numbers = sorted(numbers)
        i = 0
        j = len(numbers)-1
        while i != j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == number:
                return True
            elif sum_ > number:
                j -= 1
            else:
                i += 1
        return False
