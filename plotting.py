from graphviz import Graph
def plot_bipartite(restaurants, users, relations):
    g = Graph('G', filename='bipartite')
    
    with g.subgraph(name='cluster_0') as c:
        c.node_attr['style'] = 'filled'
        for k,v in restaurants.items():
            c.node(k)
        c.attr(label='Restaurants')
        
    with g.subgraph(name='cluster_1') as c:
        c.node_attr['style'] = 'filled'
        for k,v in users.items():
            c.node(k)
        c.attr(label='Users')
        
    for relation in relations:
        g.edge(relation['userID'],relation['placeID'])
        
    g.view()
    return g
#-----------------------------------------------------------------
def plot_graph(relations, name):
    g = Graph(name, filename=name)
    for relation in relations:
        g.edge(relation['userID'],relation['placeID'])
    g.view()
    return g
#-----------------------------------------------------------------
from graphviz import Digraph
def plot_project():
    M = Digraph()
    M.attr(size='8,4')

    M.attr('node', shape='box')
    M.node('A-MainProject.ipynb')
    M.node('B-Model-Features.ipynb')
    M.node('C-Model-DW.ipynb')

    M.attr('node', shape='ellipse')
    M.node('wrangling.py')
    M.node('modeling.py')
    M.node('graphing.py')
    M.node('plotting.py')
    M.node('neuralnetworksA4.py')
    M.node('optimizers.py')

    M.attr('node', style='filled', color='lightgrey')
    M.node('feature_vectors.sav')
    M.node('results_vectors.sav')
    M.node('deepwalk_vectors.sav')
    M.node('results_deepwalk.sav')

    M.edge('A-MainProject.ipynb','feature_vectors.sav')
    M.edge('feature_vectors.sav','B-Model-Features.ipynb')
    M.edge('B-Model-Features.ipynb','results_vectors.sav')
    M.edge('results_vectors.sav','A-MainProject.ipynb')

    M.edge('A-MainProject.ipynb','deepwalk_vectors.sav')
    M.edge('deepwalk_vectors.sav','C-Model-DW.ipynb')
    M.edge('C-Model-DW.ipynb','results_deepwalk.sav')
    M.edge('results_deepwalk.sav','A-MainProject.ipynb')

    M.edge('A-MainProject.ipynb','wrangling.py')
    M.edge('A-MainProject.ipynb','graphing.py')
    M.edge('A-MainProject.ipynb','modeling.py')
    M.edge('A-MainProject.ipynb','plotting.py')
    M.edge('B-Model-Features.ipynb','modeling.py')
    M.edge('C-Model-DW.ipynb','modeling.py')
    M.edge('modeling.py','neuralnetworksA4.py')
    M.edge('neuralnetworksA4.py','optimizers.py')

    M = M.unflatten(stagger=2)
    return M