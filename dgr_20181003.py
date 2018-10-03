>>> print(123)
123
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> print(hello world)
SyntaxError: invalid syntax
>>> print('hello world')
hello world
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> print(builtins.__doc__)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(builtins.__doc__)
NameError: name 'builtins' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input()
inputinput("Cienījamais lietotāj, lūdzu ievadi skaitli: ")

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    input()
  File "<string>", line 1, in <module>
NameError: name 'inputinput' is not defined
>>> input("Cienījamais lietotāj, lūdzu ievadi skaitli: ")
Cienījamais lietotāj, lūdzu ievadi skaitli: 100
100
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu ievadiet skaitli: ")
Cienījamais lietotāj, lūdzu ievadiet skaitli: 100
>>> vars()
{'mans_mainiigais': 100, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
