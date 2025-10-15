#  You work for Twitter, who has made major investments to fight fake news about COVID-19 spreading through their networks. 
# The company has given you a sample of a labelled dataset of tweet ex-changes betweentheir customers (TwitterUserID, list of users following IDs). 
# The task is to develop an algorithm to analyse reachability in this data set. For starters, you are tasked to find if a certain user
#  (TwitterID-A) could potentially see a post from another user (TwitterID-B).

# Allowed data structures 1. tuple, dict, list, set


#  Dataformat 1. 
# The find_path() function takes three parameters: two integers representing the start and end node ids, and, the list of the twitter users with the users they are following. Each twitter user (node) is given as a tuple (tuple[id:int, following:list[int]]).
#  (i.e. id1 follows id1,1 and id1,2 meaning you have the directed edges (id1,id1,1) and (id1,id1,2))
#  [ (<id1>, [<id1,1>, <id1,2>, ...]), ..., (<idn>, [<idn,1>, <idn,2>, ...]) ]
#  The function returns a list of integer node_ids of the path between the start and end nodes.
#  [<idstart, ..., <idend>]
#  Call: find_path(1, 5, [(1, [2]), (2, [3]),(3, [4]), (4, [5]), (5,[])])
#  Returns (list[int]): [1, 2, 3, 4, 5]

#template: 

#!/usr/bin/env python3

from typing import List, Tuple
stack = []


def find(__params__):
    '''
    TODO: Step 2: Implement the actual path finding find function.
        Add the parameters you need.
    '''

    raise NotImplementedError  # remove once implemented


def find_path(start_id: int, end_id: int, data: List[Tuple[int, List[int]]]
              ) -> List[int]:
    """
    TODO: Implement the find_path function.

    ### Parameters
    start_id : int
        ID of the starting node
    end_id : int
        ID of the target node
    data : list[tuple[int, list[int]]]
        List of tuples of the twitter user data (id:int, following:list[int])
            e.g. [(1, [2]), (2, [3]),(3, [4]), (4, [5]), (5,[])]

    ### Returns
    list[int]: List of the node id **as integers**
        of the path found between the start and end nodes
    """
    global stack
    stack = []

    for id, following in data:
        '''
        TODO: Step 1: Create and store the graph.
            The dataset gives you the IDs of the following.
            Meaning that in the above example:
                `1` is following `2`
                `2` is following `3`
                `3` is following `4`
                `4` is following `5`
                `5` is not following anyone.
            As such, the directed Graph's edges (links) will be:
                1->2, 2->3, 3->4, 4->5
            ! Pay attention to the case where a user is not following anyone.
        '''

        for f in following:
            raise NotImplementedError

    '''
    TODO: Step 3: Call your 'find` function with the parameters you defined.
    '''
    find(...)

    '''
    TODO: Step 4: return a list **of integers** of the node IDs.
        e.g. if the path requested before was 1 to 5 -> `[1,2,3,4,5]`
    '''
    raise NotImplementedError


