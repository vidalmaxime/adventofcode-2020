from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        instructions = s.split('\n')
        history = []
        acc = 0
        cursor = 0

        while cursor not in history:
            command, value = instructions[cursor].split(' ')
            history.append(cursor)
            value = int(value)
            if command == 'acc':
                acc += value
                cursor += 1
            elif command == 'jmp':
                cursor += value
            else:
                cursor += 1

        return acc