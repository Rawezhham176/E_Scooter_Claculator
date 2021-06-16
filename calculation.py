import time
import database

class Calcul:
    def __init__(self):
        self.expression = "For {} Km you have to pay {}€"

    def input_user(self):
        email = input("please enter your email adress")
        database.select_from_table("scooterUser")
        if not type(self.price) is float:
            raise Exception("Please write the correct price")
        elif not type(self.destination) is int:
            raise Exception("Please write the correct destination")
        else:
            self.result = self.price * self.destination

#0.30€ pro Minute

    def print_calc(self):
        print(self.expression.format(self.destination, self.result))
