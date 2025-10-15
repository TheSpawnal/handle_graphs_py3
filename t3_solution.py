from typing import List, Tuple

class Node:
    def __init__(self, weight: int):
        self.weight = weight
        self.following = []  # List of tuples: (neighbor_id, edge_weight)


def dijkstra(start_id: int, end_id: int, nodes: dict) -> List[int]:
    '''
    Implement Dijkstra's algorithm.

    Parameters:
    - start_id: The starting node ID.
    - end_id: The ending node ID.
    - nodes: A dictionary mapping node IDs to Node objects.

    Returns:
    - A list of node IDs representing the shortest path from start_id to end_id.
    '''
    # Initialize runs_length and ancestors
    runs_length = {node_id: float('inf') for node_id in nodes}
    ancestors = {node_id: None for node_id in nodes}
    runs_length[start_id] = 0

    unvisited = set(nodes.keys())

    while unvisited:
        # Select the unvisited node with the smallest tentative distance
        target_nodeId = None
        current_runLength = float('inf')
        for node_id in unvisited:
            if runs_length[node_id] < current_runLength:
                current_runLength = runs_length[node_id]
                target_nodeId = node_id

        if target_nodeId is None:
            # Remaining nodes are inaccessible from start_id
            break

        if target_nodeId == end_id:
            # Shortest path to end_id has been found
            break

        unvisited.remove(target_nodeId)

        current_node = nodes[target_nodeId]

        # Update runs_length for neighbors of the current node
        for neighbor_id, weight in current_node.following:
            if neighbor_id in unvisited:
                new_distance = runs_length[target_nodeId] + weight
                if new_distance < runs_length[neighbor_id]:
                    runs_length[neighbor_id] = new_distance
                    ancestors[neighbor_id] = target_nodeId

    # Reconstruct the shortest path
    if runs_length[end_id] == float('inf'):
        # No path found
        return []

    path = []
    target_nodeId = end_id
    while target_nodeId is not None:
        path.append(target_nodeId)
        target_nodeId = ancestors[target_nodeId]
    path.reverse()

    return path


def shortest_path(start_id: int, end_id: int,data: List[Tuple[int, int, List[int]]]) -> List[int]:
    """
    Implement the Dijkstra shortest path algorithm.

    ### Parameters
    `start_id` : `int`
        ID of the starting node
    `end_id` : `int`
        ID of the target node
    `data` : `list[tuple[int, int, list[int]]]`
        List of tuples of the twitter user data
            (id: int, num_likes (weight): int, following: list[int])
        e.g. `[(1, 2, [2, 3]), (2, 5, [3, 1]), (3, 6, [2])]`

    ### Returns
    list[int]: List node id **as integers**
        of the shortest path found between the start and end nodes.
    """
    # Create and store the graph using Node objects
    nodes = {}  # Maps node_id to Node object

    for id, num_likes, following in data:
        # Initialize Node objects
        nodes[id] = Node(num_likes)

    for id, num_likes, following in data:
        node = nodes[id]
        for neighbor_id in following:
            if neighbor_id in nodes:
                # Edge from id to neighbor_id with weight 1 / num_likes of neighbor_id
                neighbor_weight = nodes[neighbor_id].weight
                weight = 1 / neighbor_weight
                node.following.append((neighbor_id, weight))
            else:
                # Handle the case where neighbor_id is not in nodes
                continue  # or raise an error if appropriate

    # Call the `dijkstra` function
    path = dijkstra(start_id, end_id, nodes)

    # Return the  the list of node IDs of the shortest path 
    return path
