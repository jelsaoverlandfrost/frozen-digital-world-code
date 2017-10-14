class Celsius(object):
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        F = self._temperature * 9.0 / 5.0 + 32.0
        print self._temperature
        self._temperature = F
        return self._temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            self._temperature = -273
        else:
            self._temperature = value

    temperature = property(get_temperature, set_temperature)


c = Celsius()
print c.temperature
c.temperature = 32
print c.to_fahrenheit()
c.temperature = -300
print c.temperature
