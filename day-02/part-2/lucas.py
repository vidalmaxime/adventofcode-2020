from tool.runners.python import SubmissionPy


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        s = s.split('\n')
        count = 0
        for line in s:
            pol, letter, pw = line.split(' ')
            fst_pos, snd_pos = pol.split('-')
            if (letter[0] == pw[int(fst_pos)-1] and letter[0] != pw[int(snd_pos)-1]) or \
                (letter[0] != pw[int(fst_pos)-1] and letter[0] == pw[int(snd_pos)-1]):
                count += 1
        return count
