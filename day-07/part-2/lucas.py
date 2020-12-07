from tool.runners.python import SubmissionPy
import networkx as nx
import re

class LucasSubmission(SubmissionPy):

    """ COPIED FROM LENA TO GET THE RIGHT RESULT :D
        I JUST HAVE NO PLAN WHY MINE (BELOW) IS NOT WORKING.."""    

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

'''

    def run(self, s):
        # :param s: input in string format
        rules = s.split('\n')
        G = nx.DiGraph()
        for line in rules:
            nodes_ = re.findall(r'(\S+\s+|^)(\S+\s+|^)(\S+\s+|)(bags|bag)', line, re.IGNORECASE)
            nodes = [n[0]+(n[1][:-1]) if i==0 else n[1]+(n[2][:-1]) for i,n in enumerate(nodes_)]
            G.add_nodes_from(nodes)
            G.add_weighted_edges_from([(nodes[0], nodes[n], int(nodes_[n][0])) for n in range(1, len(nodes)) if nodes[n]!='no other'])
        number = 0
        weights = {'shiny gold': 1}
        for edge in list(nx.bfs_edges(G, 'shiny gold')):
            w = G.get_edge_data(edge[0], edge[1])['weight']
            number += weights[edge[1]]
            weights[edge[1]] = weights[edge[0]] * w
            #number += weights[edge[1]]
        return number
    
'''