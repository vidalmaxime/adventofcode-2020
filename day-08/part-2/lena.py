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
        jmps = [i for i in trail if lines[i].split()[0] == 'jmp']
        nops = [i for i in trail if lines[i].split()[0] == 'nop']
        checking = True
        for n in jmps:
            accumulator = 0
            seen = []
            i = 0
            while checking:
                if i == len(lines):
                    checking=False
                    return accumulator
                if i in seen:
                    break
                else:
                    seen.append(i)
                if i == n:
                    i+=1
                    continue
                inst = lines[i].split()
                if inst[0] == 'nop':
                    i+=1
                    continue
                elif inst[0] == 'acc':
                    accumulator += int(inst[1])
                    i+=1
                    continue
                elif inst[0] == 'jmp':
                    i+=int(inst[1])
                    continue

