from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        input_ = s.split('\n')
        state = set()
        for y in range(len(input_)):
            row = input_[y]
            for x in range(len(row)):
                cell = row[x]
                if cell == '#':
                    state.add(str([x,y,0]))
        state2 = state.copy()
        for x in state2:
            state.add(x[:-1]+', 0]')
        bounds = [0,len(input_[0]),0,len(input_),0,1,0,1]

        for i in range(6):
            state,bounds = update(state,bounds)


        return(len(state))


def neighbours(x,y,z,w):
    output = []
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            for c in [-1,0,1]:
                for d in [-1,0,1]:
                    if a==b==c==d==0:
                        continue
                    output.append(str([x+a,y+b,z+c,w+d]))
    return output

def update(state,bounds):
    bounds = bounds.copy()
    for i in range(8):
        if i % 2 == 0:
            bounds[i] = bounds[i] - 1
        else:
            bounds[i] = bounds[i] + 2
    next_ = set()
    
    for x in range(bounds[0],bounds[1]):
        for y in range(bounds[2],bounds[3]):
            for z in range(bounds[4],bounds[5]):
                for w in range(bounds[6],bounds[7]):
                    current = str([x,y,z,w])
                    count = 0
                    for cell in neighbours(x,y,z,w):
                        if cell in state:
                            count = count + 1
                        if count > 3:
                            break
                    if current in state:
                        if count in [2,3]:
                            next_.add(current)
                    else:
                        if count == 3:
                            next_.add(current)
    return next_,bounds


