import random


def _topological_sort(dag, node, visited, sorted):
    if node not in visited:
        visited.add(node)
        for child in dag[node]:
            _topological_sort(dag, child, visited, sorted)
        sorted.append(node)

def topological_sort(dag):
    visited = set()
    sorted = []
    while len(visited) < len(dag.keys()):
        node_to_check = random.choice(list(set(dag.keys()) - visited))
        if node_to_check not in visited:
            _topological_sort(dag, node_to_check, visited, sorted)
    return list(reversed(sorted))

class TestTopologicalSort(object):
    simple_dag = {'A': ['C'],
                  'B': ['C', 'D'],
                  'C': ['E'],
                  'D': ['F'],
                  'E': ['H', 'F'],
                  'F': ['G'],
                  'G': [],
                  'H': []}

    def test_topological_sort(self):
        print topological_sort(self.simple_dag)