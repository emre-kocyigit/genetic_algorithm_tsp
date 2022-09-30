# genetic_algorithm_tsp
You can use this package for Travelling Salesman Problem-related optimization problems such as Route Planning, Delivery Management etc. I implemented all important operators of Genetic Algorithm: Crossover, Mutation, Elitism, Tournament Selection etc. I created a dataset which contains 20 points, and each point has X-Y coordinates. You can use this dataset or any dataset which is in the same form without major modifying in the code.


## inputs
- dataset --> Check the training_dataset.txt file. Use same format for different datasets. 
 - Change N, according to the point number.
 
- number of generations --> iteration size
- population size --> total number of chromosomes(solutions) in a generation
- mutation rate --> it should be between 0 and 1. Usually, 0.2 or less provides better results.

## outputs
 - Improved generation which has choromosome objects. Each chromosome object contains Node objects which have id, x and y values.
 - Best chromosome of the last generation. It will be shown in a graph as a path.
 - Costs | generations graph.
