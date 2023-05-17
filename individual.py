import names
INITIAL_INCOME = 100000

class Individual:
    def get_random_name():
        return names.get_full_name()
    wealth = 0
    name = ""

    def initialIncome():
        return INITIAL_INCOME

    def __init__(self):
        self.name = Individual.get_random_name()
        
        self.wealth = Individual.initialIncome()

    def get_wealth(self):
        return self.wealth
    
    
        
    def set_wealth(self,new_wealth):
        self.wealth = new_wealth

    def earn_wealth(self, recieved):
        current_wealth = self.get_wealth()
        new_wealth = current_wealth + recieved
        self.set_wealth(new_wealth)

    def spend_wealth(self, to_spend):
        current_wealth = self.get_wealth()
        new_wealth = current_wealth - to_spend
        self.set_wealth(new_wealth)
    
    def __str__(self):
        return "Individual: Name: "+self.name+" |        Wealth: "+str(self.get_wealth())
