import statistics

class APStats():
    
    def __init__(self, data, activity, unit):
        
        self.data = data
        self.activity = activity
        self.unit = unit
    
    def mean(self):
        mean = round(statistics.mean(self.data), 1)
        print(f'The average student will take {mean} {self.unit} to {self.activity}.')

    def median(self):
        median = statistics.median(self.data)
        print(f'Half of the students will {self.activity} in {median} {self.unit} or fewer.')

    def IRQ(self, print_quanitles):
        Q1, Q2, Q3 = [round(q, 1) for q in statistics.quantiles(self.data, n=4)]
        if print_quanitles:
            print(f'{Q1 = } {self.unit}')
            print(f'{Q3 = } {self.unit}')
        print(f'The middle 50% of times to {self.activity} will vary by {Q3 - Q1} {self.unit}.')

    def stdev(self):
        stdev = round(statistics.stdev(self.data), 2)
        print(f'The typical student will {self.activity} {stdev} {self.unit} before or after the mean time.')

    def range(self):
        data_range = self.data[-1] - self.data[0]
        print(f'The range of the dataset is {data_range} {self.unit}.')

    def variance(self):
        variance = round(statistics.variance(self.data), 2)
        print(f'The variance of the dataset is {variance} {self.unit} squared.')