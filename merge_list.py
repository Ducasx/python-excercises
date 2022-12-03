def merge_lists(l1, l2):

  #"It just works" - Todd Howard
  
  if l1 == []:
    return l2
  if l2 == []:
    return l1
  
  if not (l1[0] < l2[0]):
    l1, l2 = l2, l1
  
  l3 = l1.copy()
  for x in l2:
    inserted = False
    for y in l1:
      if x < y and inserted == False:
        l3.insert(l1.index(y) ,x)
        inserted = True
    if inserted == False:
      l3.append(x)

  return l3

def swap(item1, item2):
  item3 = item1
  item1 = item2
  item2 = item3

assert merge_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9], print(merge_lists([1, 3, 6], [5, 7, 8, 9]))
assert merge_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5], print(merge_lists([1, 2, 3], [4, 5]))
assert merge_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5], print(merge_lists([4, 5], [1, 2, 3]))
assert merge_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2], print(merge_lists([2, 2, 2], [2, 2, 2]))
assert merge_lists([1, 2, 3], []) == [1, 2, 3], print(merge_lists([1, 2, 3], []))
assert merge_lists([], [1, 2, 3]) == [1, 2, 3], print(merge_lists([], [1, 2, 3]))