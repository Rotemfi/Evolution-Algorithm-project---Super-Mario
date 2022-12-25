from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.ga_creators.bit_string_vector_creator import GABitStringVectorCreator
from eckity.genetic_operators.crossovers.vector_k_point_crossover import VectorKPointsCrossover
from eckity.genetic_operators.mutations.vector_random_mutation import BitStringVectorFlipMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
import mario_evaluator
from screen_manager import Display, begin_display
from mario_plot import Information


def main():
    """Genetic algorithm for playing super mario game."""
    final_route_string = ""
    output_file = open("output.txt", "w")

    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(creators=GABitStringVectorCreator(length=mario_evaluator.level_length, bounds=(0, 2)),
                      population_size=300,
                      # user-defined fitness evaluation method
                      evaluator=mario_evaluator.SuperMarioEvaluator(),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=True,
                      elitism_rate=0.0,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          VectorKPointsCrossover(probability=0.5, k=2),
                          BitStringVectorFlipMutation(probability=0.05)
        ],
            selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(
                              tournament_size=4, higher_is_better=True), 1)
        ]),
        breeder=SimpleBreeder(),
        max_workers=1,
        max_generation=100,
        statistics=BestAverageWorstStatistics(output_stream=output_file)
    )

    # evolve the generated initial population
    algo.evolve()
    # Execute (show) the best solution
    final_route_vector = algo.execute()
    output_file.close()
    for c in final_route_vector:
        final_route_string += str(c)
    return final_route_string


if __name__ == '__main__':
    actions = main()

    # plot graph and print stats
    info = Information()
    info.read_file()
    print(f"Best sequence of actions calculated for mario: {actions}")
    print(f"Best Fitness calculated: {info.best_fitness}")
    info.plot_graph()

    # Display Game
    display = Display(mario_evaluator.level)
    begin_display()
    display.run_solution(actions)
