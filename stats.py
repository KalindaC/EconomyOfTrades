import matplotlib.pyplot as plt

class Stats:
    def __init__(self) -> None:
        pass

    @staticmethod
    def plot_wealth_distribution(individuals):
        # Sort the individuals list by wealth
        sorted_individuals = sorted(individuals, key=lambda ind: ind.get_wealth(), reverse=False)

        # Extract the wealth values from the sorted_individuals list
        wealth_values = [individual.get_wealth() for individual in sorted_individuals]

        # Create x-axis values (individual indices)
        x_values = list(range(len(sorted_individuals)))

        # Plot the wealth distribution
        plt.plot(x_values, wealth_values)
        plt.xlabel('Individual')
        plt.ylabel('Wealth')
        plt.title('Wealth Distribution')
        plt.show()