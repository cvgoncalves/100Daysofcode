
def tail(entry, n):
    """"This function gets the last n elements from entry"""
    if n <= 0:
        return []
    else:
        treat = []
        for i in entry:
            treat.append(i)
        return treat[-n:]


# Testing

#print(tail([1, 2, 3, 4, 5], 3))
#print(tail('hello', 2))

tail([1, 2, 3, 4, 5], 0)

tail([1, 2, 3, 4, 5], 3)
squares = (n**2 for n in range(10))

#print(tail(squares, 3))

tail(squares, 3)