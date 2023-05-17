from individual import Individual
from market import Market
from stats import Stats


NUMBER_OF_TRADE_ITERATIONS = 4000000
POPULATION = 1000


def main():
    market = Market()
    market_individuals = market.generate_individuals(POPULATION)
    #print("Names in list: "+ str(len(market_individuals)))
    print("Individuals in Market: "+ str(len(market_individuals)))
    for _ in range(NUMBER_OF_TRADE_ITERATIONS):
        #print("Iteration: "+ str(i))
        individual1 = Market.pick_random_individual(market_individuals)
        individual2 = Market.pick_random_individual_except_one(market_individuals,individual1)
        
        Market.trade(individual1, individual2)
    
    sorted_individuals = sorted(market_individuals, key=lambda ind: ind.get_wealth(), reverse=True)
    Stats.plot_wealth_distribution(sorted_individuals)
    for individual in sorted_individuals:
        print(individual)




# Check if the script is being run directly
if __name__ == "__main__":
    main()


    
    



