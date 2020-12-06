from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        return sum(len(set(answers.replace('\n', ''))) for answers in s.split('\n\n'))
