from tires.tires import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires_list):
        self.tires_wear = tires_list

    def needs_service(self):
        totalSum = 0
        for tire in self.tires_wear:
            totalSum += tire
        return totalSum > 3
