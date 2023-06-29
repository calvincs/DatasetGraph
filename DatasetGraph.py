import collections
import pickle
import gzip
from typing import List, Tuple


####################################################################################################
# DatasetGraph Module
#
# Author: Calvin Schultz
# Created: 2023-05
# License: MIT License
# 
# This module provides classes for managing a dataset graph, which represents a graph structure of pairs and their relationships. 
# The DatasetGraph class allows adding nodes, adding edges between pairs, loading and saving the graph to disk, 
# and retrieving next choices based on a given pair or sequence of pairs.
# 
# The DatasetGraph class provides the following functionality:
#     - Adding nodes to the graph using the add_node() method.
#     - Creating edges between pairs using the add_edge() method.
#     - Loading a dataset into the graph using the load_dataset() method.
#     - Saving the graph to disk in a compressed format using the save_to_disk() method.
#     - Loading the graph from a compressed file using the load_from_disk() method.
#     - Retrieving the next choices based on a current pair or sequence of pairs using the get_next_choices() and search_sequence() methods, respectively.
# 
# The GraphNode class represents a node in the dataset graph. 
# It contains a pair and a list of edges connecting it to other nodes.
# 
# This code is licensed under the MIT License. Feel free to modify and use it in your projects.
####################################################################################################


class GraphNode:

    def __init__(self, pair: Tuple) -> None:
        self.pair = pair
        self.edges = []


    def add_edge(self, node: 'GraphNode') -> None:
        self.edges.append(node)


class DatasetGraph:

    def __init__(self) -> None:
        self.nodes = {}


    def add_node(self, pair: Tuple) -> None:
        """
        Add a new node to the graph.

        Args:
            pair (Tuple): The pair to be added as a node.
        """
        if pair not in self.nodes:
            self.nodes[pair] = GraphNode(pair)


    def add_edge(self, pair1: Tuple, pair2: Tuple) -> None:
        """
        Add an edge between two pairs in the graph.

        Args:
            pair1 (Tuple): The first pair.
            pair2 (Tuple): The second pair.
        """
        self.add_node(pair1)
        self.add_node(pair2)
        self.nodes[pair1].add_edge(self.nodes[pair2])


    def load_dataset(self, dataset: List[List[Tuple]]) -> None:
        """
        Load a dataset into the graph.

        Args:
            dataset (List[List[Tuple]]): The dataset to be loaded into the graph.
        """
        try:
            self.dataset = dataset
            self.counter = collections.Counter(pair for entry in dataset for pair in entry)
            for entry in dataset:
                for pair1, pair2 in zip(entry[:-1], entry[1:]):
                    self.add_edge(pair1, pair2)
        except Exception as e:
            print(f"An error occurred while loading the dataset: {e}")


    def save_to_disk(self, filename: str) -> None:
        """
        Save the dataset graph to disk.

        Args:
            filename (str): The name of the file to save the graph.
        """
        try:
            with gzip.open(filename, 'wb') as f:
                pickle.dump(self.dataset, f)
        except Exception as e:
            print(f"An error occurred while saving the dataset: {e}")


    def load_from_disk(self, filename: str) -> None:
        """
        Load the dataset graph from disk.

        Args:
            filename (str): The name of the file to load the graph from.
        """
        try:
            with gzip.open(filename, 'rb') as f:
                self.load_dataset(pickle.load(f))
        except Exception as e:
            print(f"An error occurred while loading the dataset from disk: {e}")


    def get_next_choices(self, current_pair: Tuple, num_choices: int = 3) -> List[Tuple[Tuple, float]]:
        """
        Get the next choices given the current pair.

        Args:
            current_pair (Tuple): The current pair.
            num_choices (int, optional): The number of choices to retrieve. Defaults to 3.

        Returns:
            List[Tuple[Tuple, float]]: The list of next choices, each represented as a tuple of pair and probability.
        """
        try:
            if current_pair not in self.nodes:
                return []

            next_nodes = self.nodes[current_pair].edges

            # Use a set to eliminate duplicate choices
            unique_nodes = set(next_nodes)

            sorted_nodes = sorted(unique_nodes, key=lambda node: self.counter[node.pair], reverse=True)
            sorted_nodes = sorted_nodes[:num_choices]

            total_count = sum(self.counter[node.pair] for node in sorted_nodes)
            return [(node.pair, round(self.counter[node.pair] / total_count, 4)) for node in sorted_nodes]
        except Exception as e:
            print(f"An error occurred while getting the next choices: {e}")
            return []

    def search_sequence(self, sequence: List[Tuple], num_choices: int = 10) -> List[Tuple[Tuple, float]]:
        """
        Search for the next choices given a sequence of pairs.

        Args:
            sequence (List[Tuple]): The sequence of pairs.
            num_choices (int, optional): The number of choices to retrieve. Defaults to 10.

        Returns:
            List[Tuple[Tuple, float]]: The list of next choices, each represented as a tuple of pair and probability.
        """
        try:
            if len(sequence) == 0 or sequence[-1] not in self.nodes:
                return []
            next_choices = self.get_next_choices(sequence[-1], num_choices=num_choices)
            return next_choices
        except Exception as e:
            print(f"An error occurred while searching the sequence: {e}")
            return []