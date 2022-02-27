#  actions_list = self.actions(state)
#   foodList = []
#    if action not in actions_list[0]:
#         return (state[0], state[1])
#     else:
#         (x, y) = state[0]
#         theState0 = list(state[0])
#         if action == "up":
#             y = y+1
#             theState0 = (x, y)
#         elif action == "down":
#             y = y-1
#             theState0 = (x, y)
#         elif action == "right":
#             x = x+1
#             theState0 = (x, y)
#         else:
#             x = x-1
#             theState0 = (x, y)
#         counter = 0
#         for (x, y) in self.food_coords:
#             if (x, y) == tuple(theState0):
#                 foodList = list(state[1])
#                 foodList[counter] = True
#                 foodList = tuple(foodList)

#             counter = counter + 1

#         # theState = tuple(theState)
#         # print(tuple(theState))
#         return (theState0, foodList)
from problem import *


example_walls = [(4, 3), (5, 1), (5, 2)]

example_food = [(3, 1), (2, 3), (4, 5)]

example_grid_problem = GridProblem(initial_state=(7, 4),

                                   N=5, M=7,

                                   wall_coords=example_walls,

                                   food_coords=example_food)


print(example_grid_problem.result(
    state=((2, 1), (False, True, False)), action="right"))
