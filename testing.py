import unittest
from typing import List, Tuple
from DatasetGraph import GraphNode, DatasetGraph

class DatasetGraphTests(unittest.TestCase):

    def test_add_node(self):
        graph = DatasetGraph()
        pair = ('A', 'B')
        graph.add_node(pair)
        self.assertIn(pair, graph.nodes)
        self.assertIsInstance(graph.nodes[pair], GraphNode)

    def test_add_edge(self):
        graph = DatasetGraph()
        pair1 = ('A', 'B')
        pair2 = ('B', 'C')
        graph.add_edge(pair1, pair2)
        self.assertIn(pair1, graph.nodes)
        self.assertIn(pair2, graph.nodes)
        self.assertIn(graph.nodes[pair2], graph.nodes[pair1].edges)

    def test_load_dataset(self):
        graph = DatasetGraph()
        dataset = [[('A', 'B'), ('B', 'C')], [('C', 'D'), ('D', 'E')]]
        graph.load_dataset(dataset)
        self.assertEqual(len(graph.nodes), 4)

    def test_save_to_disk(self):
        graph = DatasetGraph()
        dataset = [[('A', 'B'), ('B', 'C')], [('C', 'D'), ('D', 'E')]]
        graph.load_dataset(dataset)
        filename = 'graph_data.pkl'
        graph.save_to_disk(filename)
        # Assert that the file exists
        # Assert that the file can be loaded back into the graph

    def test_load_from_disk(self):
        graph = DatasetGraph()
        filename = 'graph_data.pkl'
        graph.load_from_disk(filename)
        # Assert that the graph is loaded correctly from the file

    def test_get_next_choices(self):
        graph = DatasetGraph()
        dataset = [[('A', 'B'), ('B', 'C')], [('A', 'B'), ('D', 'E')]]
        graph.load_dataset(dataset)
        choices = graph.get_next_choices(('A', 'B'), num_choices=2)
        self.assertEqual(len(choices), 2)
        # Assert that the choices are correct

    def test_search_sequence(self):
        graph = DatasetGraph()
        dataset = [[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]]
        graph.load_dataset(dataset)
        sequence = [('A', 'B'), ('B', 'C')]
        choices = graph.search_sequence(sequence, num_choices=3)
        self.assertEqual(len(choices), 1)
        # Assert that the choices are correct

if __name__ == '__main__':
    unittest.main()
