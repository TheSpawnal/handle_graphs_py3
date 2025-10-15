
from typing import List, Tuple

def find(target_node, end_id, graph, path, visited):
    path.append(target_node)
    visited.add(target_node)
    if target_node == end_id:
        return True
    for neighbor in graph.get(target_node, []):
        if neighbor not in visited:
            if find(neighbor,end_id, graph, path,visited):
                return True
    path.pop()
    return False

def find_path(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]) -> List[int]:
    graph={}
    for id, following in data:
        graph[id] = following

    stack= [start_id]
    visited =set()
    predecessors = {}#just to reconstruct the path

    while stack:
        target_node = stack.pop()
        if target_node == end_id:
            path = [end_id]#reconstruct path from end_id to start_id
            while target_node != start_id:
                target_node = predecessors[target_node]
                path.append(target_node)
            path.reverse()
            return path
        if target_node not in visited:
            visited.add(target_node)
            for neighbor in graph.get(target_node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
                    predecessors[neighbor] = target_node

    return []#reconstruct path from end_id to start_id
