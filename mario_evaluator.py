import random
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator


def read_map(file_name):
    """
    read the map string from txt file
    :param file_name: text file
    :return: map representation as a string
    """

    data = ''
    with open(file_name, 'r') as file:
        data += file.readline()
    return data


# map params
map_file = './maps/level8.txt'
level = read_map(map_file)
level_length = len(level)


def route_creator(route_size: int) -> str:
    """
    create a route for mario level.
    :param route_size: the route length
    :return: route as string
    """
    chars = ['_', 'M', 'G', 'L']
    route_list = random.choices(chars, weights=[20, 1, 1, 1], k=route_size)
    route_str = "".join(route_list)
    return route_str


class SuperMarioEvaluator(SimpleIndividualEvaluator):
    """Evaluator class for super mario game,
    responsible for defining a fitness evaluation method and evaluating it."""

    def __init__(self, ):
        super().__init__()

    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.

        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.

        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        fitness_value = 0
        largest_path = 0
        path_length = 0
        on_air = False
        win_on_single_run = True

        for i, _ in enumerate(level):

            decision = individual.cell_value(i)

            # Jumping twice
            if i != 0 and on_air and individual.cell_value(i - 1) == 1:
                fitness_value += -1
                decision = 0

            path_length += 1
            if i != len(level) - 1:  # if we are not on the last block

                next_item = level[i + 1]

                # If we lose
                if ((not on_air) and next_item == 'G' and decision != 1) or (next_item == 'L' and decision != 2):
                    if path_length > largest_path:
                        largest_path = path_length
                    path_length = 0
                    win_on_single_run = False
                    continue

                # If we do unnecessary jump
                if next_item in ('_', 'M') and decision != 0:
                    fitness_value += -1

                if decision in ('1', '2'):
                    fitness_value += -0.5

                # If we eat mushroom
                if next_item == 'M' and decision != 1:
                    fitness_value += 3

                # If we kill a Goomba
                if i != level_length - 2 and level[i + 2] == 'G' and decision == 1:
                    fitness_value += 3

            else:
                # If we jump on flag
                if decision == 1:
                    fitness_value += 2

            on_air = decision == 1

        # If we win on a single run
        if largest_path == 0:
            if win_on_single_run:
                largest_path = level_length * 1.25
            else:
                largest_path = level_length

        # return fitness
        return largest_path + fitness_value
