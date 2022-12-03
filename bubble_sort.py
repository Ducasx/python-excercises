def bubble_sort(numbers):
  checkSwap = True
  
  for num1 in numbers:
    for num in numbers:
      if num+1 < len(numbers) and numbers[num] > numbers[num+1]:
        a = numbers[num]
        numbers[num] = numbers[num+1]
        numbers[num+1] = a
    
  return numbers


assert bubble_sort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubble_sort([2, 2, 2, 2]) == [2, 2, 2, 2]