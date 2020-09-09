Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #LIST
>>> lst=[10,20,30]
>>> lst.append(40)
>>> lst
[10, 20, 30, 40]
>>> lst.pop(2)
30
>>> lst
[10, 20, 40]
>>> lst.reverse()
>>> lst
[40, 20, 10]
>>> 
>>> 
>>> #Dictionary
>>> d={'name':'samsung','country':'India'}
>>> d
{'name': 'samsung', 'country': 'India'}
>>> d.keys()
dict_keys(['name', 'country'])
>>> d.items()
dict_items([('name', 'samsung'), ('country', 'India')])
>>> 
>>> 
>>> #Set
>>> 
>>> s={1,2,3}
>>> s
{1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s1={1,2}
>>> s1
{1, 2}
>>> print(s1.issubset(s))
True
>>> print(s.issubset(s1))
False
>>> print('s u s1=',s1.union(s))
s u s1= {1, 2, 3, 4}
>>> 
>>> 
>>> #Tuple
>>> 
>>> a=(3,4,'hello')
>>> a
(3, 4, 'hello')
>>> count=a.count('hello')
>>> print('the count of hello is:
      
SyntaxError: EOL while scanning string literal
>>> print('the count of hello is:',count)
the count of hello is: 1
>>> index=a.index(3)
>>> print('the index of 3 is:', index)
the index of 3 is: 0
>>> index=a.index(4)
>>> print('the index of 4 is:', index)
the index of 4 is: 1
>>> 
>>> 
>>> #Strings
>>> 
>>> str = "Python is awesome"
>>> str
'Python is awesome'
>>> substring="is"
>>> count=str.count(substring,3)
>>> print('the count is',count)
the count is 1
>>> 
>>> res=str.find('is')
>>> print("substring 'is':",result)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print("substring 'is':",result)
NameError: name 'result' is not defined
>>> print("substring 'is':",res)
substring 'is': 7
>>> 
>>> print(str.isdigit())
False
>>> print(str.islower())
False
>>> 
>>> str1="ABCDE FG"
>>> print(str1.lower())
abcde fg
>>> 
>>> #replace
>>> print(str1.replace('fg','xyz'))
ABCDE FG
>>> str1
'ABCDE FG'
>>> print(str1.replace('FG','xyz'))
ABCDE xyz
>>> 
>>> #split
>>> s='i love you'
>>> print(s.split())
['i', 'love', 'you']
>>> 
>>> #capitalize
>>> 
>>> string='i hate exams'
>>> cap_string=string.capitalize()
>>> print(cap_string)
I hate exams
>>> 