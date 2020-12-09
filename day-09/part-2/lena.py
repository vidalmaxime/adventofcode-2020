from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        numbers = list(map(int,s.split('\n')))
        pre = 25
        line = 25
        while line < (len(numbers)) : 
            if not sum2(numbers[(line-pre):line],numbers[line]) : 
                break
            line += 1
        value =  numbers[line]
        # Part 2
        for n1 in range(len(numbers) - 1):
            current_sum = numbers[n1]
            for n2 in range(n1 + 1, len(numbers)):
                current_sum += numbers[n2]
                if current_sum == value:
                    return min(numbers[n1:n2+1]) + max(numbers[n1:n2+1])
def sum2(li, s) :
    su = set()
    for x in range(len(li)-1) :
        for y in range(x+1, len(li)) :
            su.add(li[x]+li[y])
    return (s in su)

