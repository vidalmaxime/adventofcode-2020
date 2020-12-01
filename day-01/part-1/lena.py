from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        List = s.split()
        map_list = map(int, List)
        list_of_integers = list(map_list)
        for n, num in enumerate(list_of_integers):
            wanted = 2020 - num
            if wanted in list_of_integers[n:]:
                return (num * wanted)
