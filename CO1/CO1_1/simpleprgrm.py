# -*- coding: utf-8 -*-
"""SimplePrgrm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d6YowjcHlE29fWV1-mgFnHdW9T639LPu

*1.Review of python programming – Programs review the fundamentals of python*
"""

#Addition
3+3

#substraction
4-3

#Multplication
10*5

#devide
10/5

#square
5**2

8%2

#String
'hello'

#variable assignment
x=22
y=20
z=x+y
print(z)

#list
li=[1,2,3,4,5]
li.append(6)
li

li[3]

li[0:2]

li[2:]

#dictionaryt
(1, 2, 3, 4, 5)
t[1]
2
#sets...........
s={1,2,3,4,5,6,7}
s
d={'key1':'item1','key2':'item2','key3':'item3'}

d

d['key2']

#comparison
2>5

2<5

3==5

#tuple
t=(1,2,3,4,5)

t

t[1]

#sets...........
s={1,2,3,4,5,6,7}

s

#loop...........
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
  print(i)

i=1
while i<7 :
  print(i)
  i=i+1

#logic operations
(1>2)or(2<3)

(3>4)and(4<5)

#if else
if 2>3:
  print('false')
else:
  print('true')

#if else if
if(1==2):
  print('equal')
elif(1<2):
  print("small")
else:
  print("large")

#range
for i in range(10):
  print(i)

#functions,,,,,,,,,,,
def fun(param1="default"):
  print(param1)
fun()

def square(a):
  print(a*a)
square(5)

#lamdaa...............
def a(var):
  return var**2
a(5)