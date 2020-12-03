from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        lines = s.split('\n')
        n_pos = len(lines[0])
        #slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        slopR = [1,3,5,7]
        counters = [0, 0, 0, 0]
        counter_ = 0
        for i in range(1, len(lines)):
            counters = [counters[c]+1 if lines[i][(i*slopR[c])%n_pos]=='#' else counters[c] \
                        for c in range(len(counters))]
            if i%2==0 and lines[i][(int(i/2))%n_pos]=='#':
                counter_ += 1
        counters.append(counter_)
        return prod(counters)

def prod(l):
    if len(l) == 0:
        return 1
    else:
        return l[0]*prod(l[1:])
