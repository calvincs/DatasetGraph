# DatasetGraph

## Description
Author: Calvin Schultz<br/>
Created: 2023-05<br/>
License: MIT License<br/>

This module provides classes for managing a dataset graph, which represents a graph structure of pairs and their relationships. The DatasetGraph class allows adding nodes, adding edges between pairs, loading and saving the graph to disk, and retrieving next choices based on a given pair or sequence of pairs.

## Usage

To use the DatasetGraph module, follow these steps:

1. Import the DatasetGraph module:

    ```python
    import DatasetGraph as dg
    ```

2. Create a new DatasetGraph instance:

    ```python
    graph = dg.DatasetGraph()
    ```

3. Load a dataset into the graph using the `load_dataset()` method:

    ```python
    dataset = [
        [(1, 2), (2, 3), (3, 3), (3, 4)],
        [(1, 2), (2, 5), (5, 8), (12, 14)],
        # Add more dataset entries if needed
    ]

    graph.load_dataset(dataset)
    ```

4. Search for the next likely pair(s) after a sequence using the `search_sequence()` method:

    ```python
    sequence = [(2, 3), (3, 3)]
    next_choices = graph.search_sequence(sequence, num_choices=10)
    print(f"Next choices for the sequence {sequence} are {next_choices}")
    ```
    Returns

    ```bash
    #> Next choices for the sequence [(2, 3), (3, 3)] are [((3, 4), 1.0)]
    ```

## Other Options

Save the dataset to a file using the `save_to_disk()` method:

```python
graph.save_to_disk('dataset.pkl')
```

Load the dataset from a file using the `load_from_disk()` method:

```python
graph.load_from_disk('dataset.pkl')
```

This code is licensed under the MIT License.<br/>Feel free to modify and use it in your projects.