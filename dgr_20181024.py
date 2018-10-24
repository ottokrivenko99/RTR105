
##LENGHTS
##fruit = 'banana'
##print(len(fruit))


##LEN FUNCTIONS
##fruit = 'banana'
##x = len(fruit)
##print(x)


##LOOPING THROUGH STRINGS
##fruit = 'banana'
##index = 0
##while index < len(fruit):
##    letter = fruit[index]
##    print(index, letter)
##    index = index + 1


##LOOPING AND COUNTING
##word = 'banana'
##count = 0
##for letter in word :
##    if letter == 'a':
##        count = count + 1
##print(count)


####SLICING STRINGS
##s = 'Monty Python'
####print(s[:2])
##
##print(s[8:])



##TRING CONCATENATION
##a = 'Hello'
##b = a + 'There'
####print(b)
##c = a + ' ' + 'There'
##print(c)
##


##IN AS A LOGICAL OPERATOR
##fruit = 'banana'
##'n' in fruit
##
##fruit = 'banana'
##if 'a' in fruit :
## print('Found it!')




##STRING COMPARISION
##word = 'bananusi'
##if word == 'banana':
##    print('All right, bananas.')
##if word < 'banana':
##    print('Your word,' + word + ', comes before banana.')
##elif word > 'banana':
##    print('Your word,' + word + ', comes before banana.')
##else:
##    print('All right, bananas.')




##STRING LIBRARY
##greet = 'Hello Bob'
####zap = greet.lower()
##print(greet)



##SEARCHING A STRING
##fruit = 'banana'
##pos = fruit.find('na')
##print(pos)

##aa = fruit.find('z')
##print(aa)





##UPPER CASE
##greet = 'Hello Bob'
##nnn = greet.upper()
##print(nnn)




##SEARCH AND REPLACE
##greet = 'Hello Bob'
##nstr = greet.replace('Bob','Jane')
##print(nstr)




##STRIPING WHITESPACE
##greet = 'Hello Bob'
##greet.rstrip()
##greet.lstrip()
##greet.strip()



##PREFIXES
##line ='Please have a nice day'
####line.startswith('Please')
##line.startswith('p')




##PARSING AND EXTRACTING
##data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
##atpos = data.find('@')
##print(atpos)
##sppos = data.find('',atpos)
##print(sppos)
##host = data[atpos+ 1 : sppos]
##print(host)




