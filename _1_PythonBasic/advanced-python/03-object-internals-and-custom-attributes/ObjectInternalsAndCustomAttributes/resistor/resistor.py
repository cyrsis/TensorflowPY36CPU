class Resistor:

    __slots__ = ['resistance_ohms', 'tolerance_percent', 'power_watts']

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts
