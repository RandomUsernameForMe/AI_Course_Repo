# Install package python-constraint, not constraint !!!
import constraint

def total_coloring(graph):
    """ 
        Find total chromatic index and total coloring.
        graph - instance of networkx.Graph
        returns - total chromatic index x
        Furthermore, assign property "color" for every vertex and edge. The value of the color has to be an integer between 0 and x-1.

        TODO: The implementation of this function finds some total coloring but the number of colors may be minimal.
        Find the total chromatic index.
    """
    colors = 0
    for u in graph.nodes():
        colors += 1
        graph.nodes[u]["color"] = colors
    for u,v in graph.edges():
        colors += 1
        graph.edges[u,v]["color"] = colors
    return colors
