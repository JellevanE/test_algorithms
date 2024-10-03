import math
import numpy as np
from numpy import asarray, random



# objective function
# def objective (x):
#     return x[0]**2.0 - x[0]*8 - 4*x[0]**6 + x[0]*0.4

# complex objective
def objective(x):
    """
    Objective function for testing stochastic hill climbing.

    Args:
        x: Input value (float).

    Returns:
        Objective function value (float).
    """

    # Define your mathematical formula
    y = np.sin(x[0]) * np.exp(-x[0]**2 / 20)

    return y


def stochastic_hill_climbing(objective, bounds, n_iterations, step_size, tolerance = 1e-7):

    # randomly generate initial point
    solution = bounds[:, 0] + random.rand(len(bounds)) * (bounds[:,1] - bounds[:,0])
    print(solution)

    # evaluate initial point
    solution_evaluation = objective(solution)

    # run algorithm for n iterations
    for i in range(n_iterations):
        # take step
        step_size = step_size*0.99
        candidate_point = solution + random.rand(len(bounds)) * step_size

        # evaluate candidate
        candidate_evaluation = objective(candidate_point)

        # store candidate if it is better
        if candidate_evaluation <= solution_evaluation:
            
            # Tolerance check for minimum improvements
            if abs(candidate_evaluation - solution_evaluation) < tolerance:
                # Accept the candidate before stopping
                solution, solution_evaluation = candidate_point, candidate_evaluation
                print(f"Early stopping at iteration #{i} due to minimal improvement!")
                break

            solution, solution_evaluation = candidate_point, candidate_evaluation
            
        if i % 1000 == 0:
            print(f"candidate: #{i} \tsolution: {solution} \tevaluation: {solution_evaluation}")

    return [solution, solution_evaluation, i]


# input range, can be adjusted for more dimensional input
bounds = asarray([[-10.0, 10.0]])

# Test the algorithm with 1000 iterations and a step size of 0.1
n_iterations = 1000
step_size = 0.1

best_solution = stochastic_hill_climbing(objective, bounds, n_iterations, step_size)
print('Best solution:', best_solution)


