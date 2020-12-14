from tool.runners.python import SubmissionPy
import re

class LenaSubmission(SubmissionPy):

    def run(self, s):
        lines = s.strip().split('\n')
        mask = None
        memory = {}
        for instruction in lines:
            if instruction.startswith('mem'):
                address, value = re.findall('mem\[(\d+)\] = (\d+)', instruction)[0]
                maskes_addresses = ''.join(['X' if m == 'X' else '1' if m == '1' else v for m, v in zip(mask, format(int(address), '036b'))])
                all_addreses = [maskes_addresses]
                for i in range(maskes_addresses.count('X')):
                    new_addresses = []
                    for addr in all_addreses:
                        next_X = next(i for i,c in enumerate(addr) if c == 'X')
                        new_addresses.append(addr[:next_X] + '1' + addr[next_X+1:])
                        new_addresses.append(addr[:next_X] + '0' + addr[next_X+1:])
                    all_addreses = new_addresses
                for addr in all_addreses:
                    memory[addr] = format(int(value), '036b')
            else:
                mask = re.findall('mask = ([10X]{36})', instruction)[0]

        return sum([int(value, 2) for _, value in memory.items()])
