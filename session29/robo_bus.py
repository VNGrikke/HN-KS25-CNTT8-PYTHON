from electric_bus import ElectricBus
from autonomous_feature import AutonomousFeature


class RoboBus(ElectricBus, AutonomousFeature):

    def calculate_efficiency(self):

        electric = ElectricBus.calculate_efficiency(self)
        ai = AutonomousFeature.calculate_efficiency(self)

        return (electric + ai) / 2