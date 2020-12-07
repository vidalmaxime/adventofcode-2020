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
        
        return countBags('shiny gold', rules)

def countBags(outerBag,rules):
    count = 0
    if len(rules[outerBag]):
        for innerBag in rules[outerBag]:
            count+= rules[outerBag][innerBag]
            count += rules[outerBag][innerBag]*countBags(innerBag, rules)
        return count
    else:
        return 0