class GraphColorCSP(object):
    def __init__(self,variables,colors,adjacency):
        self.variables = variables
        self.colors = colors
        self.adjacency = adjacency
    
    def diff_satisfied(self,var1,color1,var2,color2):
        if var1 not in self.adjacency[var2]:
            return True
        elif color1 != color2:
                return True
        else:
            return False

    def is_goal(self,assignment):
        if len(self.variables) == len(assignment):
            for vertex in assignment.keys():
                for neighbor in self.adjacency[vertex]:
                    if assignment[neighbor] == assignment[vertex]:
                        return False
            return True
        else:
            return False

    
    def check_partial_assignment(self,assignment):
        for vertex in assignment.keys():
            for neighbor in self.adjacency[vertex]:
                if(neighbor in assignment.keys()):
                    if assignment[neighbor] == assignment[vertex]:
                        return False
        return True

def revise(csp,xi,xj,domains):
    revised = False
    for x in domains[xi].copy():
        # for y in domains[xj]:
            bool = csp.diff_satisfied(xi,x,xj,domains[xj])
            if not bool:
                domains[xi].remove(x)
                revised = True
    return revised


def ac3(graphcolorcsp, arcs_queue=None, current_domains=None, assignment=None):
    if arcs_queue is None:
        arcs = set()
        for var in graphcolorcsp.adjacency:
            for neighbor in graphcolorcsp.adjacency[var]:
                arcs.add((var, neighbor))
        arcs_queue = arcs
    if current_domains is None:
        