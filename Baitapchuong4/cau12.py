def oscillate(start, count):
    for i in range(start, count):
        yield i
        yield -i
for n in oscillate(-3, 5):
    print(n, end=' ')