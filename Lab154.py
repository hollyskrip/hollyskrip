#brenna and holly
class Fabric:
    def __init__(self, countryOfOrgin, color):
        self.countryOfOrgin=countryOfOrgin
        self.color=color
    def __str__(self):
        return self.countryOfOrgin+"("+str(self.color)+")"

f1=Fabric("America","blue")

print(f1)
