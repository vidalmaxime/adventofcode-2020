from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        instrs = s.split('\n')
        accu = 0
        sequence = [False]*len(instrs)
        cnt = 0
        _, problem_sequence, _ = run_program(instrs, accu, sequence, cnt)
        for i,p in enumerate(problem_sequence):
            if p and not instrs[i].startswith('acc'):
                instrs_ = instrs.copy()
                if instrs_[i].startswith('jmp'):
                    instrs_[i] = instrs_[i].replace('jmp', 'nop')
                elif instrs_[i].startswith('nop'):
                    instrs_[i] = instrs_[i].replace('nop', 'jmp')
                accu, _, cnt = run_program(instrs_, 0, [False]*len(instrs), 0)
                if cnt >= len(instrs):
                    return accu
        return -1
    
    
def run_program(instrs, accu, sequence, cnt):
    while not sequence[cnt]:
        cmd, val = instrs[cnt].split(' ')
        sequence[cnt] = True
        if cmd == 'acc':
            accu += int(val)
            cnt += 1
        elif cmd == 'jmp':
            cnt += int(val)
        else:
            cnt += 1
        if cnt >= len(instrs):
            return accu, sequence, cnt
    return accu, sequence, cnt
