#Homework 5

##1


```
#node_dict is a adjacency list representation key = node, value = list of adjacent nodes
import itertools
import string
import random

def tri_finder( node_dict ):
    tri_list = []
    for node, adj_list in node_dict.iteritems():
        #Iterate through the adjacency list

        for secondary_node in adj_list:
            #Iterate through each node in the adj list to get to the possible tertiary nodes

            for tertiary_node in node_dict[secondary_node]:
                #or each tertiary node (or a node in the adj list of a node in the adj list of our initial node)

                if node in node_dict[tertiary_node] and not any(x in tri_list for x in itertools.permutations((node, secondary_node, tertiary_node))):
                #Check if n is in the original node's adjacency list, thus theoretically completing the triangle
                # also check that no other permutation of the tuple representing the triangle exists in tri_list
                # already. If meets criteria add to the list of triangle tuples.
                    tri_list.append((node, secondary_node, tertiary_node))

    return tri_list
```

##2

I've found two kaggle competitions that I want to try to complete.

The first is this one https://www.kaggle.com/c/msdchallenge.

I think that one could use a graph approach here in training the dataset that in x instances
people who listened to song1, also listened to song2, therefore if you like song1 you might also like song2.
The stronger the weight between nodes the higher priority of suggestion it would be for someone who doesn't yet
already listen to that song.

The second is this StackOverflow problem - https://www.kaggle.com/c/predict-closed-questions-on-stack-overflow

I think that the uncertainty of this problem is what makes it interesting and will involved some text analysis / processing
to come up with an answer that will be acceptable.





