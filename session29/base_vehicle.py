from abc import ABC, abstractmethod

class BaseVehicle(ABC):
    def __init__(self,license_plate ):
        self.license_plate = license_plate
        self.__odometer = 0

    @property
    def odometer(self):
        return self.__odometer
    
    @abstractmethod
    def calculate_efficiency(self):
        pass

    def drive(self, distance):
        if distance <=0 :
            raise ValueError("Quang duong phai lon hon 0")
        
        self.__odometer += distance

    def __lt__(self, other):
        return self.__odometer < other.odometer
    
    
    @staticmethod
    def validate_license_plate(plate):
        return len(plate) == 9 and plate.startswith("29")
    