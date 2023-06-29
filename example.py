#!/usr/bin/env python3

import DatasetGraph as dg

# Create a new DatasetGraph
graph = dg.DatasetGraph()

# Load a dataset
dataset = [
        [(1, 2), (2, 3), (3, 3), (3, 4)],    
        [(1, 2), (2, 5), (5, 8), (12, 14)],
        [(6, 8), (7, 11), (18, 19)],
        [(10, 13), (12, 15), (9, 16), (14, 17), (17, 18), (4, 20)],
        [(1, 3), (5, 6), (8, 9), (11, 12), (16, 17), (19, 20), (4, 13)],
        [(3, 5), (8, 9), (13, 16), (5, 7), (9, 10), (10, 11), (2, 4), (6, 7), (12, 13), (14, 15)],
        [(4, 7), (6, 10), (1, 11), (5, 9), (12, 14), (15, 17), (4, 7), (7, 8), (8, 9)],
        [(2, 3), (3, 6), (7, 8), (11, 12), (15, 16), (17, 18), (2, 5), (7, 10), (12, 13), (14, 15)],
        [(3, 6), (8, 11), (12, 17), (4, 7), (8, 8), (9, 10), (1, 2), (2, 3), (5, 6), (7, 8), (11, 12), (16, 17), (19, 25)],
        [(6, 9), (10, 13), (2, 4), (5, 8), (12, 15), (14, 17), (3, 6), (7, 8), (9, 10), (1, 3), (2, 4), (5, 6), (7, 8)],
        [(2, 4), (4, 6), (7, 8), (10, 11), (15, 16), (18, 19), (2, 5), (7, 10), (12, 13), (14, 15), (3, 6), (7, 8), (9, 10)],
        [(4, 7), (6, 10), (3, 7)],
        [(4, 5), (5, 6), (1, 3)], 
        [(1, 2), (3, 5), (4, 6), (2, 3), (3, 3), (3, 4)],
    ]

graph.load_dataset(dataset)

# Save the dataset to a file
graph.save_to_disk('dataset.pkl')

# Load the dataset from a file
graph.load_from_disk('dataset.pkl')

# Search for the next likely pair(s) after a sequence
sequence = [(2, 3), (3, 3)]
next_choices = graph.search_sequence(sequence, num_choices=10)
print(f"Next choices for the sequence {sequence} are {next_choices}")

#> Next choices for the sequence [(2, 3), (3, 3)] are [((3, 4), 1.0)]





