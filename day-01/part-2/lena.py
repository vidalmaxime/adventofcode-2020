from tool.runners.python import SubmissionPy


class LenaSubmission(SubmissionPy):

    def run(self, s):
        List = s.split()
		map_list = map(int, List)
		list_of_integers = list(map_list)
		numbers = sorted(list_of_integers)
		l = len(numbers)
		for i in range(0,l-2):
			for j in range(i+1, l-1):
				for k in range(j+1, l):
					if numbers[i]+numbers[j]+numbers[k] == 2020:
						return numbers[i]*numbers[j]*numbers[k]
