import statistics
from matplotlib import pyplot as plt

class APStats():
    
    def __init__(self, data, unit=''):
        self.data = sorted(data)
        self.unit = unit
    
    def mean(self):
        mean = round(statistics.mean(self.data), 2)
        print(f'mean = {mean}{self.unit}.')

    def median(self):
        median = round(statistics.median(self.data), 2)
        print(f'median = {median}{self.unit}.')

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
        data_range = abs(self.data[-1] - self.data[0])
        print(f'range = {data_range}{self.unit}.')

    def variance(self):
        variance = round(statistics.variance(self.data), 2)
        print(f'variance = {variance}{self.unit} squared.')
    
    def histogram(self, name, n = max(data) - min(data)):
        plt.figure(1)
        plt.hist(self.data, n)
        plt.savefig(name)
    
    def boxplot(self, name):
        plt.figure(2)
        plt.boxplot(self.data, vert=False)
        plt.savefig(name)