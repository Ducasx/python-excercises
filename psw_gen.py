import random
from string import ascii_uppercase, ascii_lowercase, digits
special = '~!@#$%^&*()_+.'

def gen_pwd(length):

  if length < 8:
    length = 8

  psw = random.sample(ascii_lowercase, length)

  length -= 1 # lists start at 0, so length is decremented by 1

  psw = substitute(psw, ascii_uppercase, length)
  psw = substitute(psw, digits, length)
  psw = substitute(psw, special, length)

  return psw

def substitute(psw, characters, length):
  x = random.randrange(length)
  
  if psw[x] in characters:
    substitute(psw, characters) #reruns the function for a new x
  else:
    psw[x] = random.choice(characters)
  return psw

assert len(gen_pwd(7)) == 8 
assert len(gen_pwd(8)) == 8 
pwd = gen_pwd(8)
assert any(c in pwd for c in ascii_uppercase), 'uppercase letter missing'
assert any(c in pwd for c in ascii_lowercase), 'lowercase letter missing'
assert any(d in pwd for d in digits), 'digit missing'
assert any(s in pwd for s in special), 'special char missing'