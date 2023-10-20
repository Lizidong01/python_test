class A:
    def __init__(self, n):
        self.a = n
    
    def __iadd__(self, other):
        self.a = self.a + other.a
        return self
    

a1 = A(1)
a2 = A(2)
a1 += a2
print(a1.a)


class B:
    def __init__(self, n):
        self.a = n
    
    def __iadd__(self, other):
        self.a = self.a + other.a
        return self
    

b1 = B(1)
b2 = B(2)
b1 += b2
print(b1.a)