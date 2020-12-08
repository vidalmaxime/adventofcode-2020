from tool.runners.python import SubmissionPy


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        self.instructions = s.split('\n')
        self.length = len(self.instructions)
        history = []
        acc = 0
        cursor = 0

        # Follow the instructions and stop if there is a loop
        while cursor not in history:
            command, value = self.instructions[cursor].split(' ')
            if command in ['jmp', 'nop']:
                res, acc_candidate = self.force_bootstrap(cursor, history.copy(), acc)
                if res:
                    return acc_candidate
            cursor, history, acc = self.execute_command(command, value, cursor, history, acc)

    def execute_command(self, command, value, cursor, history, acc):
        history.append(cursor)
        if command == 'acc':
            acc += int(value)
            cursor += 1
        elif command == 'jmp':
            cursor += int(value)
        else:
            cursor += 1

        return cursor, history, acc

    def force_bootstrap(self, cursor, history, acc):

        # Alter the bogus command (outside of the loop as we don't expect to encounter it again)
        command, value = self.instructions[cursor].split(' ')
        command = 'jmp' if command == 'nop' else 'nop'
        cursor, history, acc = self.execute_command(command, value, cursor, history, acc)

        while cursor not in history and cursor < self.length:
            command, value = self.instructions[cursor].split(' ')
            cursor, history, acc = self.execute_command(command, value, cursor, history, acc)
        # return whether the bootstrap ran successfully
        return cursor >= self.length, acc
