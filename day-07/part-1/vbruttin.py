from tool.runners.python import SubmissionPy
import re


class VbruttinSubmission(SubmissionPy):
    def run(self, s):
        bag_of_dict = {}
        for rule in s.split('\n'):
            container = re.findall(r'^.*?(?=\sbags contain)', rule)
            contained = re.findall(r'(\d+)\s(.*?)(?=\sbags?)', rule)
            for _, bag in contained:
                bag_of_dict.setdefault(bag, [])
                bag_of_dict[bag].append(container[0])

        container_list = bag_of_dict['shiny gold']
        container_length = 0

        while len(container_list) != container_length:
            container_length = len(container_list)
            for bag in container_list:
                new_containers = bag_of_dict.get(bag, [])
                for b in new_containers:
                    if b not in container_list:
                        container_list.append(b)

        return len(container_list)
