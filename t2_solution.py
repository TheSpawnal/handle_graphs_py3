
from typing import List, Tuple

def find(target_node, end_id, path, graph, all_paths, visited):
    path.append(target_node)
    visited.add(target_node)

    if target_node == end_id:
        all_paths.append(list(path)) #copy of the curr path
    else:
        for neighbor in graph.get(target_node, []):
            if neighbor not in visited:
                find(neighbor, end_id, path, graph, all_paths, visited)
    path.pop() # backtracking
    visited.remove(target_node)

def find_paths(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]) -> List[List[int]]:

    graph={}

    for id, following in data:
        graph[id]=following#create adjacency list


    all_paths = []
    path = []
    visited=set()

    find(start_id, end_id, path, graph, all_paths, visited)


    return all_paths
