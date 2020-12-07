from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        return sum(len(set(questions.replace('\n', ''))) for questions in s.split('\n\n'))
