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
        return numbers [line]


def sum2(li, s) :
    su = set()
    for x in range(len(li)-1) :
        for y in range(x+1, len(li)) :
            su.add(li[x]+li[y])
    return (s in su)

