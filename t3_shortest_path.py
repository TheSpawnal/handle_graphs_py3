
# 3: ShortestPath
# We will develop an algorithm that finds the shortest path between a user (TwitterID-A) spreading fake news and some other user(TwitterID-B).
# Allowed data structures 3: tuple, dict, list, set.
# Dataformat3. The shortest_path function takes three parameters: two integers representing the start and end node ids, and, the list of the twitter 
# users with their number of likes and the users they arefollowing. Each twitter user(node)is given as a tuple(tuple[id:int, num_likes:int, following:list[int]]).
# All edges directed to a nodeu have a weight of 1/num_likesu
#  [ (<id1>, <num_likes1>, [<id1,1>, <id1,2>, ...]), ..., (<idn>, <num_likesn>,
#  [<idn,1>, <idn,2>, ...]) ]
#  The function returns a list of integer node_ids of the shortest paths between the start and end nodes.
#  [<idstart, ..., <idend>]
#  Call: shortest_path(1, 3, [(1, 2, [2, 3]), (2, 5, [3, 1]), (3, 6, [2])])
#  Returns (list[int]): [1, 3]

# templates:

from typing import List, Tuple


class Node:
    def __init__(self, weight: int):
        self.weight = weight
        self.following = []


def dijkstra(start_id: int):
    '''
    TODO: Implement dijkstra, change the parameters.
    '''
    raise NotImplementedError


def shortest_path(start_id: int, end_id: int,
                  data: List[Tuple[int, int, List[int]]]
                  ) -> List[int]:
    """
    TODO: Implement the dijkstra shortest path algorithm.

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

    for id, num_likes, following in data:
        '''
        TODO: Create and store the graph.
            The dataset gives you the IDs of the following.
            Meaning that in the above example:
                `1` is following `2, 3`
                `2` is following `3, 1`
                `3` is following `2`
            As such, the directed Graph's edges (links) will be:
                1->2 (cost:5), 1->3 (cost:6)
                2->3 (cost:6), 2->1 (cost:2)
                3->2 (cost:5)
            It is also possible for a user to not be following anyone.
            '''
        for f in following:
            raise NotImplementedError

    '''
    TODO: Call the `dijkstra` function with the parameters you defined.
    '''
    dijkstra(start_id)

    '''
    TODO: return a list **of integers** of the node IDs of the shortest path.
        e.g. if the path requested before was:
            start_id=1, end_id=3 -> [1,3] with a cost of 6.
            Since the other possible path would be:
                [1,2,3] with a higher cost of 5 + 6 = 11.
    '''
    raise NotImplementedError
