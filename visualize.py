import numpy as np
import matplotlib.pyplot as plt


def objective(x):
    """
    Objective function for testing stochastic hill climbing.

    Args:
        x: Input value (float).

    Returns:
        Objective function value (float).
    """

    # Define your mathematical formula here
    # For example, a multimodal function with multiple peaks:
    y = np.sin(x) * np.exp(-x**2 / 20)

    return y


# Maak een array van x-waarden in het bereik [0, 200]
x = np.linspace(-10, 10, 100)

# Bereken de corresponderende y-waarden
y = objective(x)

# Plot de grafiek
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of objective(x) function')
plt.grid(True)
plt.show()