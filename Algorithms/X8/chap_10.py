"""
5. Consider Table 10.1. Suppose the fitnesses of the 8 individuals are .61, .23, .85, .11, .27, .36, .55, and .44. Compute the normed 
fitnesses and the cumulative normed fitnesses.

normed fitness:
- 0.1784
- 0.0673
- 0.2488
- 0.0322
- 0.0789
- 0.1053
- 0.1608
- 0.1287

Cumulative normed fitness:
- 0.1784
- 0.2457
- 0.4945
- 0.5267
- 0.6056
- 0.7109
- 0.8717
- 1.0
"""

"""
6. Suppose we perform basic crossover as illustrated in Table 10.3, the parents are 01101110 and 11010101, and the starting and ending 
points for crossover are 3 and 7. Show the two children produced.

Crossover sections
Parent 1: 011 split 01110
Parent 2: 110 split 10101

Child 1: 01110101
Child 2: 11001110
"""

"""
7. Implement the genetic algorithm for finding the value of x that maximizes f(x) = sin(xπ/256), which is discussed in Section 10.2.2.
"""


import random
import math

class individual:
    def __init__(self, bit):
        self.value = bit
        self.bit = bin(bit)
        self.fitness = self.evaluate_fitness()
        self.norm_fitness = 0

    def evaluate_fitness(self):
        """
        Evaluate the fitness of an individual based on the function f(x) = sin(xπ/256).

        Returns:
            float: The fitness value of the individual.
        """
        return math.sin(self.value * math.pi / 256)

def generate_individual():
    """
    Generate a random individual consisting of 8 bits.

    Returns:
        int: A random integer representing the individual.
    """
    return random.randint(0,255)

def make_population(num: int):
    """
    Generate a population of individuals.

    Args:
        num (int): The number of individuals in the population.

    Returns:
        list: A list containing instances of the individual class.
    """
    pop = []
    for _ in range(num):
        ind_bit = generate_individual()
        ind = individual(ind_bit)
        pop.append(ind)
    return pop


def reproduce(pop: list, num: int):
    """
    Sees which individual can reproduce

    Args:
        population (list): A population to check
        num (int): Number of selections to make
    """
    total_fitness = sum(ind.fitness for ind in pop)
    normalized_fitnesses = [ind.fitness / total_fitness for ind in pop]

    # Calculate cumulative fitness values
    cumulative_fitness = 0
    cumulative_fitnesses = []
    for norm_fitness in normalized_fitnesses:
        cumulative_fitness += norm_fitness
        cumulative_fitnesses.append(cumulative_fitness)


    selected_individuals = []
    for _ in range(num):
        random_num = random.random()
        for i, cum_fit in enumerate(cumulative_fitnesses):
            if random_num <= cum_fit:
                selected_individuals.append(pop[i])
                break

    return selected_individuals

def mutate(pop: list, mutation_prob: float):
    """
    Perform mutation on individuals in the population.

    Args:
        pop (list): A list of individuals.
        mutation_prob (float): Probability of mutation for each bit.

    Returns:
        list: A list containing the offspring after mutation.
    """
    mutated_offspring = []

    for ind in pop:
        # Apply mutation
        mutated_bit = ''.join(['0' if random.random() < mutation_prob else bit for bit in ind.bit])

        # Convert mutated bit back to integer
        mutated_value = int(mutated_bit, 2)

        # Create mutated individual
        mutated_individual = individual(mutated_value)
        mutated_offspring.append(mutated_individual)

    return mutated_offspring

def crossover(pop: list, mutation_prob: float):
    """
    Perform crossover and mutation on pairs of individuals in the population.

    Args:
        pop (list): A list of individuals.
        mutation_prob (float): Probability of mutation for each bit.

    Returns:
        list: A list containing the offspring after crossover and mutation.
    """
    offspring = []

    # Randomly pair individuals
    pairs = list(zip(pop[::2], pop[1::2]))
    random.shuffle(pairs)

    for ind1, ind2 in pairs:
        # Randomly select crossover points
        crossover_points = sorted(random.sample(range(8), 2))

        if crossover_points[0] < crossover_points[1]:
            offspring1_bit = ind1.bit[:crossover_points[0]] + ind2.bit[crossover_points[0]:crossover_points[1]] + ind1.bit[crossover_points[1]:]
            offspring2_bit = ind2.bit[:crossover_points[0]] + ind1.bit[crossover_points[0]:crossover_points[1]] + ind2.bit[crossover_points[1]:]
        else:
            offspring1_bit = ind1.bit[:crossover_points[1]] + ind2.bit[crossover_points[1]:crossover_points[0]] + ind1.bit[crossover_points[0]:]
            offspring2_bit = ind2.bit[:crossover_points[1]] + ind1.bit[crossover_points[1]:crossover_points[0]] + ind2.bit[crossover_points[0]:]

        # Convert crossover bits back to integers
        offspring1_value = int(offspring1_bit, 2)
        offspring2_value = int(offspring2_bit, 2)

        # Create offspring individuals
        offspring1 = individual(offspring1_value)
        offspring2 = individual(offspring2_value)

        offspring.extend([offspring1, offspring2])

    # Perform mutation on offspring
    mutated_offspring = mutate(offspring, mutation_prob)

    return mutated_offspring

def run_program(population_size: int, mutation_prob: float, max_generations: int, fitness_threshold: float):
    """
    Perform a genetic algorithm until termination conditions are met.

    Args:
        population_size (int): The size of the population.
        mutation_prob (float): Probability of mutation for each bit.
        max_generations (int): Maximum number of generations before termination.
        fitness_threshold (float): Fitness threshold for termination.

    Returns:
        individual: The most fit individual found during the algorithm.
    """
    # Initialize population
    population = make_population(population_size)

    for generation in range(1, max_generations + 1):
        # Perform crossover and mutation
        offspring = crossover(population, mutation_prob)

        # Evaluate fitness of offspring
        for ind in offspring:
            ind.fitness = ind.evaluate_fitness()

        # Replace the population with offspring
        population = offspring

        # Check termination conditions
        most_fit_fitness = max(ind.fitness for ind in population)
        if most_fit_fitness >= fitness_threshold:
            most_fit_individual = max(population, key=lambda ind: ind.fitness)
            return most_fit_individual
        elif generation == max_generations:
            most_fit_individual = max(population, key=lambda ind: ind.fitness)
            return most_fit_individual

    # If termination conditions are not met, return the most fit individual found
    most_fit_individual = max(population, key=lambda ind: ind.fitness)
    return most_fit_individual


POPULATION_SIZE = 100
MUTATION_PROBABILITY = 0.01
MAX_GENERATIONS = 10000
FITNESS_THRESHOLD = 0.999

most_fit_individual = run_program(POPULATION_SIZE, MUTATION_PROBABILITY, MAX_GENERATIONS, FITNESS_THRESHOLD)

print("Most fit individual found:")
print("Bit:", most_fit_individual.bit)
print("Fitness:", most_fit_individual.fitness)
