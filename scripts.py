'''
SOLUTIONS TO "PROBLEM 1" EXCERCISES
'''

#################################################################### Introduction
#Say "Hello, World!" With Python
if __name__ == '__main__':
    print "Hello, World!"
    
#Python If-Else
import math, os, random, re, sys
if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2!=0:
        print("Weird") 
    else:
        if n%2==0 and n<=5 and n>=2:
            print("Not Weird")
        elif n%2==0 and n<=20 and n>=6:
            print("Weird")
        else:
            print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)
  
 #Python: Division
from __future__ import division
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)

#Loops
if __name__ == '__main__':
    n = int(raw_input())
    for x in range(n):
        print(x**2)

#Write a function
def is_leap(year):
    leap = False
    if year%4==0: 
        leap=True
        if year%100==0: 
            leap=False
            if year%400==0:
                leap=True    
    return leap

# Print Function
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    s=""
    for x in range(1,n+1):
        s+=str(x)
    print(s)

################################################################# Data Types

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
   
#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr=list(set(arr))
    arr.sort()
    print(arr[::-1][1])
   
#Nested Lists
if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append((name, score))
    a=[x[1] for x in l]
    a=list(set(a))
    a.sort()
    mm=a[1]
    secLowest_s = [x[0] for x in l if x[1]==mm]
    secLowest_s.sort()
    for x in secLowest_s:
        print(x)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a = str(sum(student_marks[query_name])/3)
    if len(a[a.find(".")+1:])==1:
        print(a+"0")
    else:
        print(a[:a.find(".")+3])
    
#Lists
if __name__ == '__main__':
    N = int(input())
    l=[]
    for x in range(N):
        cmd = input()
        if cmd.split(" ")[0]=="insert": 
            l.insert(int(cmd.split(" ")[1]), int(cmd.split(" ")[2]))
        elif cmd=="print":
            print(l)
        elif cmd.split(" ")[0]=="remove":          
            i = int(cmd.split(" ")[1])
            if i in l:
                l.remove(i)
        elif cmd.split(" ")[0]=="append":
            l.append(int(cmd.split(" ")[1]))
        elif cmd=="sort":
            l.sort()
        elif cmd=="pop":
            l.pop()  
        elif cmd=="reverse":
            l=l[::-1] 
            
#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))

################################################################# Strings    

#sWAP cASE
def swap_case(s):
    s,l="",[x.lower() if x.isupper() else x.upper() for x in s]
    for x in l:
        s+=x
    return s

#String Split and Join
import re
def split_and_join(line):
    return re.sub(" ","-",line)

#What's Your Name?
def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last))
    return None
       
#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

#Find a string
def count_substring(string, sub_string):
    counter = 0
    if len(sub_string)<=len(string):
        a=len(sub_string)
        for x in range(len(string)-a+1):
            if string[0+x:a+x]==sub_string:
                counter+=1
        return counter
    else:
        return 0

#String Validators
if __name__ == '__main__':
    s = input()
    print(any([x.isalnum() for x in s]))
    print(any([x.isalpha() for x in s]))
    print(any([x.isdigit() for x in s]))
    print(any([x.islower() for x in s]))
    print(any([x.isupper() for x in s]))


#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
def wrap(string, max_width):
    a= [string[i:i+max_width] for i in range(0,len(string),max_width)]
    s=""
    for x in a:
        s+=x+"\n"
    return s
  
#Designer Door Mat
n, m = input().split(" ") 
n,m = int(n), int(m)
odd = [x for x in range(1,100) if x%2!=0]
upperPart = []
for x in range(n):
    if x== (n-1)//2:
        print("-"*((m-len("WELCOME"))//2)  + "WELCOME" + "-"*((m-len("WELCOME"))//2))
        break
    else: 
        print("-"* ((m-odd[x]*3)//2) + odd[x]*".|." + "-"* ((m-odd[x]*3)//2))
        upperPart.append("-"* ((m-odd[x]*3)//2) + odd[x]*".|." + "-"* ((m-odd[x]*3)//2))
lowerPart = upperPart[::-1]
for x in range(len(lowerPart)):
    print(lowerPart[x])

#String Formatting
def print_formatted(number):
    w = len(str(bin(n))[2:])
    for i in range(1, n+1):
        a = str(i).rjust(w, ' ')
        b = oct(i)[2:].rjust(w, ' ')
        c = hex(i)[2:].upper().rjust(w, ' ')
        d = bin(i)[2:].rjust(w, ' ')
        print (a, b, c, d)   
       
#Alphabet Rangoli
import re
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = []
def print_rangoli(size):
    let = alphabet[:size]
    totLen = (len(let)+len(let)-1)*2
    for x in range(len(let)*2-1):
        if x == n-1:           
            s = ""
            for y in let[::-1]:
                s+=y +" "
            for y in let[1:]:
                s+=y+" "
            s = re.sub(" ", "-", s[:-1])
            print(s)
            break    
        else:
            rSide=let[::-1][:x+1][::-1]
            lSide=rSide[1:][::-1]
            line= lSide+rSide 
            s=""
            for y in line:
               s+=y+" "
            s = re.sub(" ", "-", s[:-1])
            print("-"*((totLen-len(s))//2) + s + "-"*((totLen-len(s))//2))
            upper.append("-"*((totLen-len(s))//2) + s + "-"*((totLen-len(s))//2))        
    lower=upper[::-1]
    for x in lower:
        print(x)

#Capitalize!
def solve(s):
    s=s.lower()
    l=s.split(" ")   
    l= [x[0].upper()+x[1:] if x!="" else x for x in l]
    q=""
    for x in l:
        q+=x +" "
    return q[:-1] 

#The Minion Game
vowels= ["A","E","I","O","U"] 
consonants = [x.upper() for x in "abcdefghijklmnopqrstuvwxyz" if x.upper() not in vowels]
def minion_game(s):
    kevin, stuart = 0, 0
    length = len(s)
    for x in range(length):
        if s[x] in vowels:
            kevin+=length-x     
        if s[x] in consonants:
            stuart+=length-x   
    if kevin!=stuart:   
        if kevin>stuart:
            print("Kevin "+ str(kevin))
        else:
            print("Stuart " + str(stuart))
    else:
        print("Draw")        
    
#Merge the Tools!
def merge_the_tools(string, k):   
    for x in range(0,len(string),k):
        l=[el for el in string[x:x+k]]
        l = list(dict.fromkeys(l).keys())
        print(''.join(l))
        
################################################################# Sets

#Introduction to Sets
def average(array):
    array=list(dict.fromkeys(array).keys())
    return sum(array)/len(array)
    
#No Idea!
n, m = list(map(int, input().split()))
arr, setA, setB = list(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split())) 
happ = 0
for x in arr:
    if x in setA:
        happ+=1
    elif x in setB:
        happ-=1

#Symmetric Difference
if __name__ == '__main__':
    n, arr = input(), list(dict.fromkeys(list(map(int, input().split()))).keys())
    n1, arr1 = input(), list(dict.fromkeys(list(map(int, input().split()))).keys())
    l = [x for x in arr if x not in arr1] + [x for x in arr1 if x not in arr]
    l.sort()
    for x in l:
        print(x)

#Set .add()
n, l = int(input()), []
for x in range(n):
    a=input()
    if a not in l:
        l.append(a)
print(len(l))

#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
cmd = int(input())
for x in range(cmd):
    a=input().split()
    if a[0]=="pop" and len(s)>0:
        s.pop()      
    elif a[0]=="remove" and a[0] in s:
        s.remove(int(a[1]))
        print("y")
    else:
        s.discard(int(a[1]))
print(sum(s))

#Set .union() Operation
n, s, n1, s1 = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
print(len(s | s1))

#Set .intersection() Operation
n, arr, n1, arr1 = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
print(len(arr & arr1))

#Set .difference() Operation
n, arr, n1, arr1 = int(input()), set(map(int, input().split())),int(input()), set(map(int, input().split()))
print(len(arr - arr1))

#Set .symmetric_difference() Operation
n, arr, n1, arr1 = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
print(len(arr ^ arr1))

#Set Mutations
n, arr, cmds = int(input()), set(map(int, input().split())), int(input())
for x in range(cmds):
    cmd, arr1 = input().split()[0], set(map(int, input().split()))
    if cmd =="intersection_update":
        arr.intersection_update(arr1)
    if cmd =="update":
        arr.update(arr1)
    if cmd =="difference_update":
        arr.difference_update(arr1)
    if cmd =="symmetric_difference_update":
        arr.symmetric_difference_update(arr1)    
print(sum(arr))

#The Captain's Room
n, arr = int(input()), list(map(int, input().split()))
d = {}
for x in set(arr):
    d[x]=0
for x in range(len(arr)):
    d[arr[x]]+=1
for x in list(d.keys()):
    if d[x]== min(list(d.values())):
        print(x)

#Check Subset
n=int(input())
for x in range(n):
    n1, arr1, n2, arr2 = int(input()), set(map(int, input().split())), int(input()), set(map(int, input().split()))
    if arr1.issubset(arr2):
        print(True)
    else:
        print(False)
        
#Check Strict Superset 
arr, n = set(map(int, input().split())), int(input())
for x in range(n):
    arr1=set(map(int, input().split()))
    if x==n-1 and arr1.issubset(arr):
        print(True)
    if not arr1.issubset(arr):
        print(False)
        break
   



################################################################# 
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################























    

