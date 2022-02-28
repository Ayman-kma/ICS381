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
def visualize_route_problem_solution(problem, goal_node, file_name):
    states = get_path_states(goal_node)
    x_coords= []
    y_coords= []
    for x,y in problem.map_coords.values():
        x_coords.append(x)
        y_coords.append(y)
    plt.scatter(x_coords,y_coords, marker = 's',color ='blue')
    IandG = [problem.map_coords[problem.initial_state],problem.map_coords[goal_node.state]]
    x_coords= [IandG[0][0],IandG[1][0]]
    y_coords= [IandG[0][1],IandG[1][1]]
    plt.scatter(x_coords,y_coords, marker = 's', color=["red","green"])
    for state in problem.map_coords.keys():
        for action in problem.actions(state):
            x = problem.map_coords[action][0] - problem.map_coords[state][0]
            y = problem.map_coords[action][1] - problem.map_coords[state][1]
            plt.arrow(problem.map_coords[state][0],problem.map_coords[state][1], x, y)
    
    for i in range(len(states)-1):
        x = problem.map_coords[states[i+1]][0] - problem.map_coords[states[i]][0]
        y = problem.map_coords[states[i+1]][1] - problem.map_coords[states[i]][1]
        plt.arrow(problem.map_coords[states[i]][0],problem.map_coords[states[i]][1], x, y,color ='magenta')

    plt.savefig(file_name)

    plt.show()
    print("Show is not cool")
    plt.close()


def visualize_grid_problem_solution(problem, goal_node, file_name):
    states = get_path_states(goal_node)
    wall = problem.wall_coords
    food = problem.food_coords
    plt.scatter(problem.initial_state[0][0],problem.initial_state[0][1], marker = 's', color ='green' )
    x_coords= []
    y_coords= []
    for pair in wall:
        x_coords.append(pair[0])
        y_coords.append(pair[1])
    plt.scatter(x_coords,y_coords, marker = 's', color ='black' )
    x_coords= []
    y_coords= []
    for pair in food:
        x_coords.append(pair[0])
        y_coords.append(pair[1])
    plt.scatter(x_coords,y_coords , marker = 'o', c ='red' )
    for i in range(len(states)-1):
        x = states[i+1][0][0] - states[i][0][0]
        y = states[i+1][0][1] - states[i][0][1]
        plt.arrow(states[i][0][0],states[i][0][1], x, y,color ='magenta')

    plt.savefig(file_name)
    print("Show is cool")
    plt.show()
    print("Show is not cool")
    plt.close() 