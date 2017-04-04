def _visit(graph, vertex, path):
    path.add(vertex)
    for neighbor in graph.get(vertex, {}):
        if neighbor in path or _visit(graph, neighbor, path):
            return True
    path.remove(vertex)
    return False


def cyclic(graph):
    path = set()
    for v in graph:
        if _visit(graph, v, path):
            return True
    return False


class TestCycleDetection(object):
    graph_with_cycle = {
        'A': {'B','C'},
        'B': {'D'},
        'C': {'D'},
        'D': {'A'}
    }

    graph_with_no_cycle = {
        'A': {'B', 'C'},
        'B': {'D'},
        'C': {'D'},
        'D': {}
    }

    def test_cycle_detection(self):
        assert cyclic(self.graph_with_cycle)
        assert not cyclic(self.graph_with_no_cycle)

    def test_dfs_cycle_detection(self):
        assert cyclic_dfs(self.graph_with_cycle)
        assert not cyclic_dfs(self.graph_with_no_cycle)