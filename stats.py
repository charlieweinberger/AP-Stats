import statistics
from matplotlib import pyplot as plt

class APStats():
    
    def __init__(self, data, unit=''):
        self.data = sorted(data)
        self.unit = unit
    
    def mean(self):
        mean = round(statistics.mean(self.data), 2)
        print(f'{mean = }{self.unit}.')

    def median(self):
        median = round(statistics.median(self.data), 2)
        print(f'{median = }{self.unit}.')

    def five_point_summary(self):
        Q1, Q2, Q3 = [round(q, 2) for q in statistics.quantiles(self.data, n=4)]
        print(f'five point summary: {self.data[0]}, {Q1}, {Q2}, {Q3}, {self.data[-1]}')

    def IRQ(self):
        Q1, Q2, Q3 = [round(q, 2) for q in statistics.quantiles(self.data, n=4)]
        print(f'IRQ = {Q3 - Q1}{self.unit}.')

    def stdev(self):
        stdev = round(statistics.stdev(self.data), 2)
        print(f'standard deviation = {stdev}{self.unit}.')

    def range(self):
        data_range = round(abs(self.data[-1] - self.data[0]), 3)
        print(f'range = {data_range}{self.unit}.')

    def variance(self):
        variance = round(statistics.variance(self.data), 2)
        print(f'{variance = }{self.unit} squared.')
    
    def percentile(self, x):
        if x == '': return
        percentile = len(self.data) * x / 100
        print(f'{percentile = }')

    def z_score(self, x):
        if x == '': return
        z_score = round((x - statistics.mean(self.data)) / statistics.stdev(self.data), 2)
        print(f'{z_score = }')

    def all(self, x=''):
        self.mean()
        self.median()
        self.five_point_summary()
        self.IRQ()
        self.stdev()
        self.range()
        self.variance()
        self.percentile(x)
        self.z_score(x)