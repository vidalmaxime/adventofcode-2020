from tool.runners.python import SubmissionPy
import networkx as nx
import re


class LucasSubmission(SubmissionPy):

    def run(self, s):
        # :param s: input in string format
        rules = s.split('\n')
        G = nx.DiGraph()
        for line in rules:
            nodes = re.findall(r'(\S+\s+|^)(\S+\s+|)(bags|bag)', line, re.IGNORECASE)
            nodes = [n[0]+(n[1][:-1]) for n in nodes]
            G.add_nodes_from(nodes)
            G.add_edges_from([(nodes[n], nodes[0]) for n in range(1, len(nodes))])
        
        return len(nx.nodes(nx.dfs_tree(G, 'shiny gold')))-1
