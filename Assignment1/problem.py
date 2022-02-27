class Problem:
    def __init__(self, initial_state, goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        raise NotImplementedError(self.__class__.__name__)

    def result(self, state, action):
        raise NotImplementedError(self.__class__.__name__)

    def is_goal(self, state):
        if state == self.goal_state:
            return True
        else:
            return False

    def action_cost(self, state1, action, state2):
        return 1

    def h(self, node):
        return 0


class RouteProblem(Problem):
    def __init__(self, initial_state, goal_state=None,
                 map_graph=None,
                 map_coords=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.map_graph = map_graph
        self.map_coords = map_coords

    def actions(self, state):
        neighbours = []
        for (x, y) in self.map_graph:
            if x == state:
                neighbours.append(y)
        return neighbours

    def result(self, state, action):
        for (x, y) in self.map_graph:
            if x == state and y == action:
                return action
        return state

    def action_cost(self, state1, action, state2):
        if(state1, state2) in self.map_graph:
            return self.map_graph[(state1, state2)]
        else:
            return 0

    def h(self, node):
        if node == self.goal_state:
            return 0
        else:
            (x1, y1) = self.map_coords[node.state]
            (x2, y2) = self.map_coords[self.goal_state]
            distance = ((x1-x2) ** 2 + (y1-y2) ** 2)**(1/2)
            return distance


class GridProblem(Problem):
    def __init__(self, initial_state, N, M, wall_coords, food_coords):
        food_eaten = []
        for i in range(0, len(food_coords)):
            food_eaten.append(False)
        food_eaten = tuple(food_eaten)
        self.initial_state = (initial_state, food_eaten)
        self.N = N
        self.M = M
        self.wall_coords = wall_coords
        self.food_coords = food_coords
        self.goal_state = None

    def actions(self, state):
        list = []
        (x, y) = state[0]
        if x > 0 and y > 0:
            if (y+1) <= self.N and (x, (y+1)) not in self.wall_coords:
                list.append("up")
            if (y-1) >= 1 and (x, y-1) not in self.wall_coords:
                list.append("down")
            if (x+1) <= self.M and (x+1, y) not in self.wall_coords:
                list.append("right")
            if (x-1) >= 1 and (x-1, y) not in self.wall_coords:
                list.append("left")
        return list

    def result(self, state, action):
        actions_list = self.actions(state)
        if action not in actions_list:
            return state
        x, y = state[0]
        if x > 0 and y > 0:
            if (action == "up"):
                y = y+1
            if (action == "down"):
                y = y-1
            if (action == "right"):
                x = x+1
            if (action == "left"):
                x = x-1
            tuple_coords = (x, y)
            tuple_bools = state[1]
            if (tuple_coords in self.wall_coords):
                return state
            if (tuple_coords in self.food_coords):
                index = self.food_coords.index(tuple_coords)
                bool_list = list(tuple_bools)
                bool_list[index] = True
                tuple_bools = tuple(bool_list)
            return (tuple_coords, tuple_bools)
        return state

    def is_goal(self, state):
        listy = list(state[1])
        for item in listy:
            if item == False:
                return False
        return True

    def action_cost(self, state1, action, state2):
        return 1

    def h(self, node):
        distance = 1000000
        x2, y2 = node.state[0]
        if self.is_goal(node.state):
            return 0
        else:
            counter = 0
            for i in range(len(node.state[1])):
                if node.state[1][i] == False:
                    x1, y1 = self.food_coords[i]
                    manhattan = abs(x1 - x2) + abs(y1 - y2)
                    if distance > manhattan:
                        distance = manhattan
                # x1, y1 = self.food_coords[node.state[1].index(False)]
                # distance = 100000000000000000
                # for tub in enumerate(self.food_coords):
                #     print("line 135")
                #     if len(node.state[1]) > counter:
                #         print("line 137")
                #         if node.state[1][counter] == False:
                #             print("line 139")
                #             x1, y1 = tub[1]
                #             manhattan = abs(x1 - x2) + abs(y1 - y2)
                #             if distance > manhattan:
                #                 distance = manhattan
                #         counter = counter + 1

            return distance
