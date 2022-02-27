from node import Node
import heapq
import matplotlib.pyplot as plt


def expand(problem, node):
    s = node.state
    nodes = []
    for action in problem.actions(s):
        sP = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, sP)
        nodes.append(Node(state=sP, parent_node=node,
                          action_from_parent=action, path_cost=cost))
    return nodes


def get_path_actions(node):
    actions = []
    if node is None:
        return []
    elif node.parent_node is None:
        return []
    else:
        while node.parent_node is not None:
            print(node.action_from_parent)
            actions.insert(0, node.action_from_parent)
            node = node.parent_node
        return actions


def get_path_states(node):
    states = []
    if node is None:
        return []
    else:
        while node.parent_node is not None:
            states.insert(0, node.state)
            node = node.parent_node
        states.insert(0, node.state)
        return states


class PriorityQueue:
    def __init__(self, items=(), priority_function=(lambda x: x)):
        self.priority_function = priority_function
        self.pqueue = []
        # add the items to the PQ
        for item in items:
            self.add(item)

    def add(self, item):
        pair = (self.priority_function(item), item)
        heapq.heappush(self.pqueue, pair)

    def pop(self):
        return heapq.heappop(self.pqueue)[1]

    def __len__(self):
        return len(self. pqueue)


def best_first_search(problem, f):
    node = Node(problem.initial_state)
    frontier = PriorityQueue([node], priority_function=f)
    reached = {problem.initial_state: node}
    while frontier:
        new_node = frontier.pop()
        if problem.is_goal(new_node.state):
            return new_node
        for child in expand(problem, new_node):
            s = child.state
            if (s not in reached.keys()) or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return None


def best_first_search_treelike(problem, f):
    node = Node(state=problem.initial_state)
    frontier = PriorityQueue([node], priority_function=f)
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            frontier.add(child)
    return None


def breadth_first_search(problem, treelike=False):
    if(treelike):
        return best_first_search_treelike(problem, f=lambda Node: Node.depth)
    else:
        return best_first_search(problem, f=lambda Node: Node.depth)


def depth_first_search(problem, treelike=False):
    if(treelike):
        return best_first_search_treelike(problem, f=lambda Node: -Node.depth)
    else:
        return best_first_search(problem, f=lambda Node: -Node.depth)


def uniform_cost_search(problem, treelike=False):
    if(treelike):
        return best_first_search_treelike(problem, f=lambda Node: Node.path_cost)
    else:
        return best_first_search(problem, f=lambda Node: Node.path_cost)


def greedy_search(problem, h, treelike=False):
    if(treelike):
        return best_first_search_treelike(problem, f=lambda node: h(node))
    else:
        return best_first_search(problem, f=lambda node: h(node))


def astar_search(problem, h, treelike=False):
    if(treelike):
        return best_first_search_treelike(problem, f=lambda node: h(node) + node.path_cost)
    else:
        return best_first_search(problem, f=lambda node:  h(node) + node.path_cost)
