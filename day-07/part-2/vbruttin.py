from tool.runners.python import SubmissionPy
import re


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        bag_of_dict = {}
        for rule in s.split('\n'):
            container = re.findall(r'^.*?(?=\sbags contain)', rule)
            contained = re.findall(r'(\d+)\s(.*?)(?=\sbags?)', rule)
            bag_of_dict[container[0]] = contained

        current_bags = [(1, 'shiny gold')]
        total = 0

        while current_bags:
            tmp = []
            for n, bag in current_bags:
                new_bags = bag_of_dict.get(bag)
                if new_bags is not None:
                    for m, b in new_bags:
                        m = int(m)
                        tmp.append((n * m, b))
                        total += n * m
            current_bags = tmp

        return total
