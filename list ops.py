## list operatyions:
list1=[1,2,3,'a']


'''
>>> list1
[1, 2, 3, 'a']
>>> 
>>> 
>>> str(list1)
"[1, 2, 3, 'a']"
>>> 
>>> dir(list1)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 


>>> list1.append('abc')
>>> list1
[1, 2, 3, 'a', 'abc']
>>> 
>>> list1.append("def")
>>> list1
[1, 2, 3, 'a', 'abc', 'def']
>>> 

>>> len(list1)
6

>>> type(list1)
<class 'list'>

>>> list1.extend('charles')
>>> list1
[1, 2, 3, 'a', 'abc', 'def', 'c', 'h', 'a', 'r', 'l', 'e', 's']

>>> list2=[2,3,4]
>>> list3=[4,5,6]
>>> 
>>> list1.append(list3)
>>> list1
[1, 2, 3, 'a', 'abc', 'def', 'c', 'h', 'a', 'r', 'l', 'e', 's', [4, 5, 6]]
>>> 
>>> list1.extend
<built-in method extend of list object at 0x0000000003665148>
>>> list1.extend(list2')
	     
SyntaxError: EOL while scanning string literal
>>> 
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 'a', 'abc', 'def', 'c', 'h', 'a', 'r', 'l', 'e', 's', [4, 5, 6], 2, 3, 4]
>>> 

>>> l1=[1,2,3]
>>> l1
[1, 2, 3]
>>> l2=[4,5,6]
>>> l2
[4, 5, 6]
>>> l1+l2
[1, 2, 3, 4, 5, 6]
>>> 

>>> l1+[l2]
[1, 2, 3, [4, 5, 6]]
>>> 

'''
