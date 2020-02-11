import numpy as np
import matplotlib.pyplot as plt

"""
Module contains a parent class with general things common to the Julia set and the Mandelbrot set.
Fractals are generated by finding the last number before the sequence z_{n+1} = z_{n} + C turned out
to be diverging, where C is a constant explored over the given interval of complex numbers and z_{0} = 0.
"""

class Fractal:
    """
    Class initializes fractals, checks if values from a complex plane make convergent sequences,
     and prints the fractal graph.
    Attributes:
        iteration_limit: int - number which says how many iterations we want to go through to check
            whether the sequence is diverging.
        accuracy: int - number of points between -2.025 and 0.6 for x, and from -1.125 to 1.125 for y,
            which we consider in our visualization.
    """
    def __init__(self, iteration_limit: int, accuracy: int) -> None:
        self.iteration_limit = iteration_limit
        self.accuracy = accuracy

    def last_convergent(self, *args, **kwargs):
        """
        The method returns the last number before a sequence turned out to be diverging.
        It differs between Mandelbrot and Julia sets, so is intentionally skipped in the parent class.
        """
        pass

    def last_convergent_array(self) -> [[complex]]:
        """
        Generate a 2D array with the numbers of the last number
        before the sequence turned out to be diverging.
        """
        x_array = np.linspace(-2.025, 0.6, self.accuracy)
        y_array = np.linspace(-1.125, 1.125, self.accuracy)
        constants = np.zeros((self.accuracy, self.accuracy), dtype=complex)

        for x_index in range(len(x_array)):
            for y_index in range(len(y_array)):
                constants[x_index, y_index] = complex(x_array[x_index], y_array[y_index])

        last_convergent_array = [[self.last_convergent(element) for element in row] for row in constants]
        return last_convergent_array

    def plot(self):
        """Plot the graph of the fractal."""
        last_convergent_array = np.array(self.last_convergent_array())
        plt.imshow(last_convergent_array.T, cmap='RdGy', extent=[-2.025, 0.6, -1.125, 1.125])
        plt.xlabel = "Real part"
        plt.ylabel = "Imaginary part"
        plt.show()