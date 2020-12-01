from tool.runners.python import SubmissionPy


class JessySubmission(SubmissionPy):

    def run(self, s):
        entries = sorted(map(int, s.split()))
        n_entries = len(entries)
        target = 2020
        for i in range(n_entries - 1):
            j = i + 1
            k = n_entries - 1
            while j < k:
                temp = entries[i] + entries[j] + entries[k]
                if temp == target:
                    return entries[i] * entries[j] * entries[k]
                if temp > target:
                    k -= 1
                else:
                    j += 1
