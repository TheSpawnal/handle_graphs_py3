# 2/FindAllPaths
# Our task is to find all the possible paths from which a (TwitterID-A) could have seen a post by a user (TwitterID-B). 
# For each path a vertice should be visited only once as the graph may contain cycles.
# Allowed data structures 2: tuple, dict, list, set
# Dataformat2. Thefind_paths()function takes the same parameters and data format as our fist task mentioned earlier.. 
# But,  returns a list of lists (list[list[int]]) of all possible paths from start to end.
#  [ [idstart>, ..., <idend>], [<idstart>, ..., <idend>], ...]
# Call: find_paths(1, 3, [(1, [2, 3]), (2, [3, 1]), (3, [2])])
# Returns (list[list[int]]): [[1, 3], [1, 2, 3]]
# template:

from typing import List, Tuple

def find(__params__):
    '''
    TODO: Step 3: Implement the actual multi-path finding find function.
        Add the parameters and returns you need.
        For each path a vertice can be visited only once.
    '''

    raise NotImplementedError  # remove once implemented


def find_paths(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]
               ) -> List[List[int]]:
    """
    TODO: Implement the multi-path finding method.

    ### Parameters
    start_id : int
        ID of the starting node
    end_id : int
        ID of the target node
    data : list[tuple[int, list[int]]]
        List of tuples of the twitter user data (id:int, following:list[int])
            e.g. [(1, [2, 3]), (2, [3, 1]), (3, [2])]

    ### Returns
    list[list[int]]: List of lists of the node id **as integers**
        of the paths found between the start and end nodes.
    """

    for id, following in data:
        '''
        TODO: Step 1: Create and store the graph.
            The dataset gives you the IDs of the following.
            Meaning that in the above example:
                `1` is following `2, 3`
                `2` is following `3, 1`
                `3` is following `2`
            As such, the directed Graph's edges (links) will be:
                1->2, 1->3
                2->3, 2->1
                3->2
            It is also possible for a user to not be following anyone.
        '''
        for f in following:
            raise NotImplementedError

    '''
    TODO: Step 3: Call your `find` function with the parameters you defined.
    '''
    find(...)

    '''
    TODO: Step 4: return a list of lists **of integers** of the node IDs.
        e.g. if the path requested before was 1 to 3 -> [[1,3],[1,2,3]].
        The order of the lists is not important
    '''
    raise NotImplementedError
