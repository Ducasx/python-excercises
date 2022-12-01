def find_and_replace(text, old_text, new_text):
    #converts text into an array from string
    arrayed_text = []
    for letter in text:
        arrayed_text.append(letter)

    #converts old_text into an array from string
    arrayed_old_text = []
    for letter in old_text:
        arrayed_old_text.append(letter)

    #converts new_text into an array from string
    arrayed_new_text = []
    for letter in new_text:
        arrayed_new_text.append(letter)

    for x in arrayed_text:
        if(x == arrayed_old_text[0]):
            index = arrayed_text.index(x)
            jndex = index
            check = False
            for y in arrayed_old_text:
                if not (y == arrayed_text[index] and not check):
                    check = True
                index += 1
            if not check:
                index = jndex
                for y in arrayed_old_text:
                    arrayed_text.pop(index)
                for y in new_text:
                    arrayed_text.insert(index, y)
                    index += 1
    
    text = ''.join(arrayed_text)
    return text

assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
assert find_and_replace('THE FOX AND THE DOG', 'fox', 'dog') == 'THE FOX AND THE DOG'
assert find_and_replace('The fox and fxx.', 'fox', 'dog') == 'The dog and fxx.'
assert find_and_replace('The fox', 'fox', 'crocodile') == 'The crocodile'
assert find_and_replace('The crocodile', 'crocodile', 'fox') == 'The fox'