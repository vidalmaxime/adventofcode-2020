from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        instrs = s.split('\n')
        accu = 0
        sequence = [False]*len(instrs)
        cnt = 0
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
        return accu
