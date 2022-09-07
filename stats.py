import statistics
from matplotlib import pyplot as plt

class APStats():
    
    def __init__(self, data):
        self.data = sorted(data)
    
    def mean(self):
        print(f'mean = {round(statistics.mean(self.data), 2)}')

    def median(self):
        print(f'median = {round(statistics.median(self.data), 2)}')

    def five_point_summary(self):
        Q1, Q2, Q3 = [round(q, 2) for q in statistics.quantiles(self.data, n=4)]
        print(f'five point summary: {self.data[0]}, {Q1}, {Q2}, {Q3}, {self.data[-1]}')

    def IRQ(self):
        Q1, Q2, Q3 = [round(q, 2) for q in statistics.quantiles(self.data, n=4)]
        print(f'IRQ = {Q3 - Q1}')

    def stdev(self):
        print(f'standard deviation = {round(statistics.stdev(self.data), 2)}')

    def range(self):
        print(f'range = {round(abs(self.data[-1] - self.data[0]), 3)}')

    def variance(self):
        print(f'variance = {round(statistics.variance(self.data), 2)}')
    
    def percentile(self, x):
        if x == '': return
        print(f'percentile = {len(self.data) * x / 100}')

    def z_score(self, x):
        if x == '': return
        print(f'z_score = {round((x - statistics.mean(self.data)) / statistics.stdev(self.data), 2)}')

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