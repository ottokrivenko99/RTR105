>>> fhand = open('text1.txt', 'r')
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> xfiles = open('text1.txt')
>>> for fg in xfile:
	print(fg)

	

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    for fg in xfile:
NameError: name 'xfile' is not defined
>>> fhand = open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    fhand = open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> fhand = open('text1.txt')
>>> count = 0
>>> for line in fhand
SyntaxError: invalid syntax
>>> fhand = open('text.txt')

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fhand = open('text.txt')
IOError: [Errno 2] No such file or directory: 'text.txt'
>>> fhand = ('text1.txt')
>>> inp = fhand.read()

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    inp = fhand.read()
AttributeError: 'str' object has no attribute 'read'
>>> fhand = open('text1.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startseith('From:')
	
SyntaxError: invalid syntax
>>> fhand = open('text1.txt')
>>> for line in fhand:
	line = line.rstrip()
	if not line.startswith('from:') :
		continue
	print(line)

	
>>> fname = input('text1.txt: ')
text1.txt: fhand = open(fname)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fname = input('text1.txt: ')
  File "<string>", line 1
    fhand = open(fname)
          ^
SyntaxError: invalid syntax
