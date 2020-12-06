from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        return sum(len(set.intersection(*(set(answers) for answers in group.split())))
                   for group in s.split('\n\n'))
