import GeneticAlgorithm as GA
import Chromosome as Ch

# following libraries for graphs
import numpy as np
import matplotlib.pyplot as plt


# parameters
numbers_of_generations = 200  # in other words, iteration size
population_size = 100  # this shows how many solutions will be available in a generation
mut_rate = 0.2  # mutation rate for solution diversity. It should be btw 0 and 1. 0.2 means --> 20%
dataset = Ch.dataset  # locations info in a list form. Each element of the list is a Node object, which as id, x, y info


# main function for genetic algorithm
def genetic_algorithm(num_of_generations, pop_size, mutation_rate, data_list):
    new_gen = GA.initialization(data_list, pop_size)  # first generation is created with initialization function

    costs_for_plot = []  # this list is only for Cost-Generations graph. it will constitute y-axis of the graph

    for iteration in range(0, num_of_generations):
        new_gen = GA.create_new_generation(new_gen, mutation_rate)  # create a new generation in each iteration
        # print the cost of first chromosome of each new generation to observe the change over generations
        print(str(iteration) + ". generation --> " + "cost --> " + str(new_gen[0].cost))
        costs_for_plot.append(GA.find_best(new_gen).cost)  # append the best chromosome's cost of each new generation
        # to the list to plot in the graph

    return new_gen, costs_for_plot


def draw_cost_generation(y_list):
    x_list = np.arange(1, len(y_list)+1)  # create a numpy list from 1 to the numbers of generations

    plt.plot(x_list, y_list)

    plt.title("Route Cost through Generations")
    plt.xlabel("Generations")
    plt.ylabel("Cost")

    plt.show()


def draw_path(solution):
    x_list = []
    y_list = []

    for m in range(0, len(solution.chromosome)):
        x_list.append(solution.chromosome[m].x)
        y_list.append(solution.chromosome[m].y)

    fig, ax = plt.subplots()
    plt.scatter(x_list, y_list)  # alpha=0.5

    ax.plot(x_list, y_list, '--', lw=2, color='black', ms=10)
    ax.set_xlim(0, 1650)
    ax.set_ylim(0, 1300)

    plt.show()


last_generation, y_axis = genetic_algorithm(
    num_of_generations=numbers_of_generations, pop_size=population_size, mutation_rate=mut_rate, data_list=dataset
)

best_solution = GA.find_best(last_generation)

draw_cost_generation(y_axis)

draw_path(best_solution)

