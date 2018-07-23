# Name: ...
# CSE 140
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
import operator
import random


###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_node("A")
practice_graph.add_node("B")
practice_graph.add_node("C")
practice_graph.add_node("D")
practice_graph.add_node("E")
practice_graph.add_node("F")

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("D", "C")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")
practice_graph.add_edge("C", "F")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

def draw_practice_graph():
    """Draw practice_graph to the screen."""
    nx.draw(practice_graph)
    plt.show()

draw_practice_graph()


###
### Problem 1b
###

# (Your code goes here.)
rj = nx.Graph()

rj.add_node("Nurse")
rj.add_node("Juliet")
rj.add_node("Tybalt")
rj.add_node("Capulet")
rj.add_node("Romeo")
rj.add_node("Friar Laurence")
rj.add_node("Benvolio")
rj.add_node("Montague")
rj.add_node("Escalus")
rj.add_node("Mercutio")
rj.add_node("Paris")

rj.add_edge("Nurse", "Juliet")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Tybalt", "Juliet")
rj.add_edge("Capulet", "Juliet")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Friar Laurence", "Romeo")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Paris", "Mercutio")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Paris", "Capulet")



assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

def draw_rj():
    """Draw the rj graph to the screen and to a file."""
    nx.draw(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

draw_rj()




###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    closeFriends = friends(graph, user)
    
    farFriends = set
    
    for a in closeFriends:
        farFriends = farFriends.union(friends(graph, a))
    
    farFriends.remove(user)
    for a in closeFriends:
        if(a in farFriends):
            farFriends.remove(a)
    
    #print(farFriends)
    return farFriends

assert friends_of_friends(rj, "Mercutio") == set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common."""
    cFriends = friends(graph, user1).intersection(friends(graph, user2))
    #print(cFriends)
    return cFriends
    

assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])

assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map from each user U to the number of friends U has in common with the given user.
    The map keys are the users who have at least one friend in common with the
    given user, and are neither the given user nor one of the given user's friends.
    Take a graph G for example:
        - A and B have two friends in common
        - A and C have one friend in common
        - A and D have one friend in common
        - A and E have no friends in common
        - A is friends with D
    number_of_common_friends_map(G, "A")  =>   { 'B':2, 'C':1 }
    """
    numFriendsDict = {}
    for a in friends_of_friends(graph, user):
        numFriendsDict[a] = 0
    #print(numFriendsDict)
    # Find common friends and set them to 0 in the dictionary, for every 
    #friend of the common friends if they match a friend of the user add 1 to dictionary
    for node in friends_of_friends(graph, user):
        numFriendsDict[node] += len(common_friends(graph, user, node))

    #print(numFriendsDict)
    return numFriendsDict

assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}

assert number_of_common_friends_map(rj, "Mercutio") == { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map):
    """Given a map whose values are numbers, return a list of the keys.
    The keys are sorted by the number they map to, from greatest to least.
    When two keys map to the same number, the keys are sorted by their
    natural sort order, from least to greatest."""
    #print("MAAAAAAAPPPPP")
    #print(map)
    sortedList = []
    max = 0
    for a in map:
        if map[a] > max:
            max = map[a]
            
    for i in range(int(100*(max+1))):
        tempList = []
        for a in map:
            if int(100*(map[a])) == i:
                tempList.append(a)
        tempList.sort(reverse = True)
        #print(tempList)
        for z in tempList:
            sortedList.append(z)
    #print(sortedList)
    sortedListReverse = []
    p = len(sortedList) - 1
    for i in range(len(sortedList)):
        sortedListReverse.append(sortedList[p])
        p = p - 1
        
    #print("SORTED")
    #print(sortedListReverse)

    return sortedListReverse

assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the number of common friends.
    """
    recommendedFriends = number_map_to_sorted_list(number_of_common_friends_map(graph, user))
    #print(recommendedFriends)
    return recommendedFriends


assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']

assert recommend_by_number_of_common_friends(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map from each user U to the friend influence, with respect to the given user.
    The map only contains users who have at least one friend in common with U,
    and are neither U nor one of U's friends.
    See the assignment for the definition of friend influence.
    """
    #print("INFLUENCEMAP")
    #for each common friend calculate the weight of that friend and add it to each user
    numFriendsDict = {}
    for a in friends_of_friends(graph, user):
        numFriendsDict[a] = 0
    #print(numFriendsDict)
    # Find common friends and set them to 0 in the dictionary, for every 
    #friend of the common friends if they match a friend of the user add 1 to dictionary
    for node in friends_of_friends(graph, user):
        for a in common_friends(graph, user, node):
            numFriendsDict[node] += 1/len(friends(graph, a))
    #print(numFriendsDict)
    return numFriendsDict

######ISSUE HERE BASED ON DIFFERENCE IN ORDERING DESPITE NO MENTION OF A SPECIFIC ORDER BEING REQUIRED##########
    
assert influence_map(rj, "Mercutio") == { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the influence measurement.
    """
    influenceRecommend = number_map_to_sorted_list(influence_map(graph, user))
    #print("INFLUENCE")
    #print(influenceRecommend)
    return influenceRecommend

assert recommend_by_influence(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###

sameList = []
differentList = []
for a in rj.nodes():
    if recommend_by_number_of_common_friends(rj, a) == recommend_by_influence(rj, a):
        sameList.append(a)
    else:
        differentList.append(a)
sameList.sort()
differentList.sort()

print("Unchanged Recommendations:", sameList)
print("Changed Recommendations: ", differentList)


###
### Problem 5
###

# (Your code goes here.)
facebook = nx.read_edgelist("facebook-textFixed.txt",  nodetype = int)


assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090
print("DONE")


###
### Problem 6
###


###
### Problem 7
###


###
### Problem 8
###


###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").


