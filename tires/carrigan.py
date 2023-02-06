from tires.tires import Tire


class CarriganTire(Tire):
    def __init__(self, tires_list):
        self.tires_wear = tires_list

    def needs_service(self):
        for tire in self.tires_wear:
            if tire > 0.9:
                return True
        return False
