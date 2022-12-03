def maximum(t):
    maximum = t[0]
    for num in t:
        if num > maximum:
            maximum = num

    return maximum

def minimum(t):
    minimum = t[0]
    for num in t:
        if num < minimum:
            minimum = num

    return minimum

def somma(t):
    sum = 0
    for num in t:
        sum += num
    return sum

def prod(t):
    prod = 1
    for num in t:
        prod *= num
    return prod

def moda(t):
    appearances = {}

    for num in t: #creates a dictionary number:times_it_appears
        if not (num in appearances):
            x = 0
            for y in t:
                if y == num:
                    x += 1
            appearances[num] = x

    moda = None
    for num in appearances:
        if moda == None or appearances[num] > appearances[moda]:
            moda = num

    return moda

def avg(t):
    return somma(t)/len(t)

def median(t):
    t = sorted(t)
    if len(t) % 2 == 1:
        return t[(len(t)) // 2]
    else:
        return (t[(len(t) // 2) - 1] + t[(len(t) // 2)]) / 2

t = [1, 2, 3, 4, 5]
assert maximum(t) == 5
assert minimum(t) == 1
assert somma(t) == 15
assert prod(t) == 120
assert round(avg(t), 2) == 3
assert median(t) == 3
assert moda([1, 2, 3, 1, 2, 1, 1, 1, 2]) == 1
assert moda([1, 2, 3, 3, 3, 1, 2, 1, 2, 3, 3, 3]) == 3

# mescolare t non deve cambiare la mediana

import random
random.seed(42)
t = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for _ in range(5):
  random.shuffle(t)
  assert median(t) == 6