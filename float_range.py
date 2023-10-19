class FloatRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += self.step
            return self.start
        raise StopIteration

for each in FloatRange(1.0, 2.0, 0.1):
    print(each)
