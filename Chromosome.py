import math


class Node:  # Node = Location = Point
    def __init__(self, id, x, y):
        self.x = float(x)
        self.y = float(y)
        self.id = int(id)


# 1 Open a file and create a data list using the info in the file
file_name = "training_dataset"  # write path if the file is not in the same directory
dataset = []


with open(file_name, "r") as f:
    for line in f:  # check each line
        new_line = line.strip()  # remove spaces at the beginning and the end if they are available
        new_line = new_line.split(" ")  # split a string into a list
        id, x, y = new_line[0], new_line[1], new_line[2]  # check dataset file to see why id,x,y = 0,1,2
        dataset.append(Node(id=id, x=x, y=y))  # Create a Node object with id, x, y and add to the data list

N = 20  # Total number of unique points, including starting point


# This function will be run once at the beginning of the program to create a distance matrix
def create_distance_matrix(node_list):
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    # classical matrix creation with two for loops
    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[0])-1):
            # calculate euclidean distance btw each points and add to the matrix
            # a^2 = b^2 + c^2
            matrix[node_list[i].id][node_list[j].id] = math.sqrt(
                pow((node_list[i].x - node_list[j].x), 2) + pow((node_list[i].y - node_list[j].y), 2)
            )
    return matrix


matrix = create_distance_matrix(dataset)  # calculate all distances among all points and create a matrix
# This matrix is needed to decrease the runtime and complexity of general flow.


# Chromosome = Solution = Path
# Chromosome will contain Node list. This will be used in crossover, mutation operations etc,
# Chromosome representation --> chr_representation is only for displaying the route in a simple/clear way
# Chromosome cost will be used to compare the chromosomes
# We want to minimize the cost. So, lower cost is better!
class Chromosome:
    def __init__(self, node_list):
        self.chromosome = node_list

        chr_representation = []
        for i in range(0, len(node_list)):
            chr_representation.append(self.chromosome[i].id)
        self.chr_representation = chr_representation

        distance = 0
        for j in range(1, len(self.chr_representation) - 1):  # get distances from the matrix
            distance += matrix[self.chr_representation[j]-1][self.chr_representation[j + 1]-1]
        self.cost = distance

        self.fitness_value = 1 / self.cost






