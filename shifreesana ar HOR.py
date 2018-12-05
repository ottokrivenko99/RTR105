Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> original = "to be or not to be"
>>> type(original)
<type 'str'>
>>> original[0]
't'
>>> ord(original[0])
116
>>> bin(ord(original[0]))
'0b1110100'
>>> key = 5
>>> original[0] ^ key

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    original[0] ^ key
TypeError: unsupported operand type(s) for ^: 'str' and 'int'
>>> ord(original[0]) ^ key
113
>>> chr(ord(original[0]) ^ key)
'q'
>>> original
'to be or not to be'
>>> key
5
>>> message = ""
>>> N = len(original)
>>> for i in range(N):
	message = message + chr(ord(original[i]) ^ key)

	
>>> 
>>> message
'qj%g`%jw%kjq%qj%g`'
>>> 
>>> result = ""
>>> key1 = 6
>>> for i in range(N):
	message = message + chr(ord(message[i]) ^ key1)

	
>>> result
''
>>> for i in range(N):
	message = message + chr(ord(message[i]) ^ key1)

	
>>> rsult

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    rsult
NameError: name 'rsult' is not defined
>>> result
''
>>> result = ""
>>> key1 = 5
>>> or i in range(N):
	message = message + chr(ord(message[i]) ^ key1)
	
SyntaxError: invalid syntax
>>> for i in range(N):
	message = message + chr(ord(message[i]) ^ key1)


>>> result
''
>>> 
