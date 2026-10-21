class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num +n

    @staticmethod
    def add(a,b):
        return a+b

a = Math(5)
print(a.num)

a.addtonum(6)
print(a.num)


print(Math.add(2,9))

# -------------------------

class WeatherUtils:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


fahrenheit = WeatherUtils.celsius_to_fahrenheit(30)

print(f"30 degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

celsius = WeatherUtils.fahrenheit_to_celsius(86)
print(f"86 degrees Fahrenheit is equal to {celsius} degrees Celsius.")
