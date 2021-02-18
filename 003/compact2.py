class Compact:
    """"Gets an input and compacts the input in an iterator"""

    def __init__(self, number_list):
        self.res = set(number_list)
        self.r = []
        for i in self.res:
            self.r.append(i)
    def __iter__(self):
        yield self.r







x = [1, 1, 2, 2, 3, 3]

y = [1, 2, 2, 3, 4]

z = []

c = Compact(n**2 for n in [1, 2, 2])

print(Compact(y).r)
print(Compact(x).r)
print(Compact(z).r)

print(c.r)

print(iter(c.r) is c.r)
