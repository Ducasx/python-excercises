import random

def shuffle(values):
  values2 = []

  random.seed(random.randint(0,999))

  for x in range(len(values)):
    y = random.choice(values)
    values2.append(y)
    values.remove(y)

  return values2

# Perform this test ten times:
testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testData1 = shuffle(testData1)
print(testData1)
# Make sure the number of values hasn't changed:
assert len(testData1) == 10
# Make sure the order has changed:
assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Make sure that when re-sorted, all the original values are there:
assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []