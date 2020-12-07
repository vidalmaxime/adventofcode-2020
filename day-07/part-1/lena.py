from tool.runners.python import SubmissionPy
import re

class LenaSubmission(SubmissionPy):

    def run(self, s):
        reOuter = re.compile('^([\w ]*) bags contain ')
        reInner = re.compile('(\d{1,}) ([\w ]*) bag(?:s)?')
        rules = {}
        #create new dict with colors and numbers
        for rule in s.split('\n'):
            outer = reOuter.findall(rule)[0]
            rules[outer] = {}
            inner = reInner.findall(rule)
            for bag in inner:
                rules[outer][bag[1]]=int(bag[0])

        count = 0
        for rule in rules:
            trail = []
            if lookIn(rule,trail, rules):
                count += 1
        return count-1

    
def lookIn(outerBag, trail, rules):
    if 'shiny gold' in outerBag:
        return True
    else:
        for innerBag in rules[outerBag]:
            if innerBag not in trail:
                trail.append(innerBag)
                if lookIn(innerBag, trail, rules):
                    return True
        return False