from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        numbers = list(map(int,s.split()))
        for i in range(25, len(numbers)):
            if not self.is_sum(numbers[i], numbers[i-25:i]):
                invalid_nr = numbers[i]
                invalid_ix = i
        for min_ in range(invalid_ix):
            res = self.find_set(invalid_nr, numbers[min_:invalid_ix])
            if res:
                return res
        return -1
    
            
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

    def find_set(self, number, numbers):
        current_sum = numbers[0]
        for i in range(1, len(numbers)):
            current_sum += numbers[i]
            if current_sum == number:
                return min(numbers[0:i+1]) + max(numbers[0:i+1])
            if current_sum > number:
                return False
        