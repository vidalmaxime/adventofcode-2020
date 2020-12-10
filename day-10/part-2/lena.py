from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        s = list(sorted(map(int,s.split('\n'))))
        s = [0]+s+[max(s)+3]
        paths = {}
        sorted_s = sorted(s, reverse=True)
        for n, el in enumerate(sorted_s):
            # Add the initial max joltage entry
            if len(paths) == 0:
                paths[el] = 1
            else:
                i, ways = 1, 0
                while (n-i >= 0) and (sorted_s[n-i] - el <= 3):
                    ways += paths[sorted_s[n-i]]
                    i += 1
                paths[el] = ways
        return(paths[min(paths)])