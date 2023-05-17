import random
from individual import Individual


class Market:
    def __init__(self):
        self.individuals = []

    @staticmethod
    def trade(individual1, individual2):
        if individual1.get_wealth() < 1:
            return  # Individuals with less than 1 wealth cannot trade

        price = Market.tradePrice(individual1)

        if price <= individual1.get_wealth():
            individual1.spend_wealth(price)
            individual2.earn_wealth(price)

    @staticmethod
    def tradePrice(spender):
        allowed_range = range(
            int(spender.get_wealth() / 2)
        )  # no one can spend more than half their wealth
        return random.choice(allowed_range)

    @staticmethod
    def generate_individuals(population):
        individuals = []
        for _ in range(population):
            # name = i
            individual = Individual()
            individuals.append(individual)
        return individuals

    @staticmethod
    def pick_random_individual(individuals):
        return random.choice(individuals)

    @staticmethod
    def pick_random_individual_except_one(individuals, excluded_individual):
        individuals_except_excluded = [
            ind for ind in individuals if ind != excluded_individual
        ]
        if individuals_except_excluded:
            return random.choice(individuals_except_excluded)
        else:
            return None
