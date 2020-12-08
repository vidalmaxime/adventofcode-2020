from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        lines = s.split('\n')
        acc = 0
        i = 0
        trail = []
        while i not in trail:
            [instruction, value] = lines[i].split(" ")
            trail.append(i)
            if instruction == 'acc':
                acc+= int(value)
                i+=1
            if instruction == 'jmp':
                i+= int(value)
            if instruction == 'nop':
                i+=1
        
        return acc