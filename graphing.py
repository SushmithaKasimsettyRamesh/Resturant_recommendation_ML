import easygraph as eg
def create():
    return eg.Graph()
#-----------------------------------------------------------------
def add_nodes(graph, data):
    for k,v in data.items():
        graph.add_node(k, node_attr=v)
    print(len(data.keys()), 'nodes added.')
    return graph
#-----------------------------------------------------------------
def add_edges(graph, data):
    for rating in data:
        graph.add_edge(rating['userID'],rating['placeID'],
                       edges_attr={'rating':rating['rating'],
                                   'food_rating':rating['food_rating'],
                                   'service_rating':rating['service_rating']})
    print(len(data), 'edges added.')
    return graph
#-----------------------------------------------------------------
from easygraph.functions.graph_embedding import deepwalk
def embeddingDW(G):
    return deepwalk(G)
#-----------------------------------------------------------------
def obtain_inputs(embeddings, r, u):
    vector = []
    vector.extend(embeddings[r])
    vector.extend(embeddings[u])
    return vector
#-----------------------------------------------------------------
import numpy as np
def obtain_inputs_outputs(embeddings, data):
    inputs = []
    outputs1 = []
    outputs2 = []
    outputs3 = []
    for rating in data:
        inputs.append(obtain_inputs(embeddings, rating['placeID'], rating['userID']))
        outputs1.append([int(rating['rating'])])
        outputs2.append([int(rating['food_rating'])])
        outputs3.append([int(rating['service_rating'])])
    return np.array(inputs), np.array(outputs1), np.array(outputs2), np.array(outputs3)
#-----------------------------------------------------------------
import random
def pick_random(data):
    found = False
    while(not found):
        k,v = random.choice(list(data.items()))
        if ('U' in k):
            found = True
            print('User: {}'.format(k))
            for similar_node in v:
                if ('U' not in similar_node[0]) and (similar_node[1] > 0.5):
                    print(similar_node)
#-----------------------------------------------------------------
from easygraph.functions.drawing import draw_kamada_kawai
def plot_kamada(graph):
    draw_kamada_kawai(graph, rate=1)
#-----------------------------------------------------------------
from easygraph.functions.drawing import draw_SHS_center
def plot_shs(graph):
    draw_SHS_center(graph, [])
#-----------------------------------------------------------------