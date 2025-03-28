# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:01:32 2024
@author: sa4422

Lecture 2 notes
Datatypes and classes
Can make own classes and define operations that are legal for it using class intialisation

"""
# DATA TYPE 1 - INT
a = 2 # a statement and an assignment operator, a bucket with a name "a"
# allocate memory path (shortcut is named "a")
# NB goes from right to left , NOT A RELATION

type(a)
# a is an integer - it is not just a number, it is a datatype (human construct)
# in computing terms is a class "int"  


# DATA TYPE 2 - FLOAT
b = 3 
a+b

b/2
type(b/2) # float point number, has a decimal point 

c = b/2 #result of division always a float 

3*3.0 # gets you a float

#what about integer division
5//2

#to find remainder 
5%2 #remainder of the division operation returned here 
#can use to chekc if something is odd or even

b**2 

#DATA TYPE 3 - STRING
#denoted by quotes, agnostic to type of quotes (just be consistent open close)
s = "hi"

s+s
s + " " + s
s + 3 #but this is an error


3*s

#butttt 
3/2*s #not viable because float output 
3//1*s #is viable because int output

'3'*2 #viable - but output maybe unexpected as treated as string

x = 3

type(3)
float(3)
int(3.0) #does NOT round, just cuts off decibel

int('33')
str(3)

#DATA TYPE 4 - booleans (bool - evaluates to True of False)
3 < 1 #this is an expression to be evaluated
#true is 1 , false is 0 
# so 
3 < False
3 > True

3 == 1 #this is equivalence - it is an equivalence expression

# If things are not equivalent we can explore and express that in a number of ways! 
3!= 1 

not True

x = 3<1

y = 2==4 

x or y

x and y
not x and y 
not x and not y 
# only way AND is true is when both are true
# only way OR is false if both are false 

#DATA TYPE 5 - a list() will be covered in the next sesssion


# PLAIN TEXT FILES - a note
#.txt extention
#for example in notebook 

#we save plain text files using .py files
#e.g 
print('hello world')

x = input("Write something: ") #takes it as a string, convert later
print("You wrote: ", x)






 



