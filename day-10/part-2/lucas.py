from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        adapters = sorted(list(map(int,s.split())))
        #adapters = [0] + adapters + [adapters[-1]+3]
        return self.count_arrangements(adapters, 0)
        
        
    def count_arrangements(self, adapters, outlet_charge):
        diff_dict = {outlet_charge: 1}
        for number in adapters:
            diff_dict[number] = 0
            for difference in range(number-3, number):
                if difference in diff_dict:
                    diff_dict[number] += diff_dict[difference]
        return diff_dict[adapters[-1]]
