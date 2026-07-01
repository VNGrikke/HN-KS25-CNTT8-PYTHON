from base_vehicle import BaseVehicle


class ElectricBus(BaseVehicle):

    def calculate_efficiency(self):
        result = 100 - (self.odometer * 0.005)

        if result < 50:
            return 50.0

        return result