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

################################################################# Collections

#collections.Counter()
n, arr, n1 = int(input()), list(map(int, input().split())), int(input())
rev = 0
for x in range(n1):
    j,k = list(map(int, input().split()))
    if j in arr:
        arr.remove(j)
        rev+=k
print(rev)

#DefaultDict Tutorial
from collections import defaultdict
n, m = list(map(int, input().split()))
a, b = [input() for x in range(n)], [input() for x in range(m)]
for x in b:
    s=""
    for y in range(len(a)):
        if x==a[y]:
            s+=str(y+1) + " "
    if s=="":
        s="-1"       
    print(s)        

#Collections.namedtuple()
from collections import namedtuple
n, cols = int(input()), list(map(str, input().split()))
uff = [x for x in range(len(cols)) if cols[x]=="MARKS"]
grades=0
for x in range(n):
    grades+= int(list(map(str, input().split()))[uff[0]]) 
print(round(grades/n,2))

#Collections.OrderedDict()
from collections import OrderedDict
n = int(input())
d = {}
for x in range(n):
    s = input()
    q = s.split()[-1]
    s=s[:-len(q)] 
    if s not in list(d.keys()):
        d[s]=0    
    d[s] += int(q)    
for x in d:
    print(x + str(d[x]))

#Word Order
n = int(input())
l = [input() for x in range(n)]
print(len(set(l)))
d=dict.fromkeys(l,0)
for x in l:
    d[x]+=1
s=""
for x in d.values():
    s+=str(x) + " "  
print(s)

#Collections.deque()
from collections import deque
n = int(input())
d=deque()
for x in range(n):
    cmd = input().split()    
    if cmd[0]=="append":
        d.append(cmd[1])    
    elif cmd[0]=="appendleft":
        d.appendleft(cmd[1])    
    elif cmd[0]=="popleft":
        d.popleft()    
    elif cmd[0]=="pop":
        d.pop()
s=""
for x in d:
   s+=str(x) + " " 
print(s)

#Company Logo
import math, os, random, re, sys
import collections
from operator import itemgetter
if __name__ == '__main__':
    s = input()
    l = [x for x in s]
    d = dict.fromkeys(l, 0)
    for x in l:
        d[x]+=1    
    a=sorted([(list(d.values())[x],list(d.keys())[x]) for x in range(len(list(d)))], key = itemgetter(0), reverse=True )  
    count = 0
    for x in range(len(a)):
        if count==2:
            try:
                while a[count][0]==a[count+1][0]:
                    count+=1
            except Exception:    
                pass
            count+=1
            break
        else:
            count+=1
    a=a[:count]    
    if len(set([str(x[0]) for x in a]))==1: #tutti stessi numeri, lett diverse
        a = sorted(a, key = itemgetter(1))[:3]
        tot=a    
    elif len(set([str(x[0]) for x in a]))==2:
        fs, sc = [x[1] for x in a if x[0]==max([x[0] for x in a])], [x[1] for x in a if x[0]==min([x[0] for x in a])]       
        fs.sort()
        fs = [(max([x[0] for x in a]),fs[x]) for x in range(len(fs))]
        sc.sort()
        sc = [(min([x[0] for x in a]),sc[x]) for x in range(len(sc))]
        tot = fs + sc
        tot = tot[:3]                
    elif len(set([str(x[0]) for x in a]))==3: 
        fs, md, sc = [x[1] for x in a if x[0]==max([x[0] for x in a])], [x[1] for x in a if x[0]!=max([x[0] for x in a]) and x[0]!=min([x[0] for x in a])], [x[1] for x in a if x[0]==min([x[0] for x in a])]         
        fs.sort()
        fs = [(max([x[0] for x in a]),fs[x]) for x in range(len(fs))]
        sc.sort()
        sc = [(min([x[0] for x in a]),sc[x]) for x in range(len(sc))]
        md.sort()
        l=[x[0] for x in a]
        l.remove(min([x[0] for x in a]))
        l.remove(max([x[0] for x in a]))
        l=l[0]
        md = [(l,md[x]) for x in range(len(md))]  
        tot = fs + md +sc
        tot = tot[:3]       
a=tot      
for x in range(len(a)):
    print(str(a[x][1])+ " " + str(a[x][0]))

#Piling Up! 
'''
I had problems debugging my code, because the console was not able to FIT large datasets, neither the ones provided by HackerRank itself.
Thus i wasn't able to see if my previous code had Memory Errors, Runtime Errors or provided just Wrong Answers.
This was my previous code:
t = int(input())
for x in range(t):
    n, s = int(input()), list(map(int, input().split())) 
    for iStop in range(len(s)-1):
        if s[iStop] <= s[iStop+1]:
            break
    s=s[iStop+1:]
    for jStop in range(len(s)-1, -1, -1):
        if s[jStop] <= s[jStop-1]:
            break
    s=s[:jStop]
    if len(s)==0:
        print("Yes")
    else:
        print("No") 
Looking up online i came up with this very logical way of assessing the problem (the one below), that made me think that cutting my very large list with "s=s[:jStop]"
twice might have raised a MemoryError that althogh i was not able to receive for the problem stated above.
'''
t = int(input())
for x in range(t):
    n, s = int(input()), list(map(int, input().split())) 
    cc = 0
    while cc < len(s) - 1 and s[cc] >= s[cc + 1]:
        cc+=1    
    while cc < len(s) - 1 and s[cc] <= s[cc + 1]:
        cc += 1
    if cc==len(s)-1:
        print("Yes")    
    else:
        print("No")

################################################################# Date and Time

#Calendar Module
import calendar
a = list(map(int, input().split()))
days = {"0":"MONDAY","1":"TUESDAY","2":"WEDNESDAY","3":"THURSDAY","4":"FRIDAY","5":"SATURDAY","6":"SUNDAY",}
print(days[str(calendar.weekday(a[2],a[0],a[1]))])

#Time Delta
import math, os, random. re, sys, datetime
def time_delta(t1, t2):
    delta = abs(datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") - datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z"))
    return str(delta.total_seconds())[:-2]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

################################################################# Errors and Exceptions

#Exceptions
n = int(input())
for x in range(n):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ValueError as e:
        print ("Error Code:",  e)
    except ZeroDivisionError as e:
        print ("Error Code:",  e)

################################################################# Built-Ins

#Zipped!
n, m = list(map(int, input().split()))
lists= [input().split() for x in range(m)]
for x in range(len(lists)):
    lists[x] = [float(y) for y in lists[x]]
a = [x for x in zip(*lists)]
for x in a:
    print(float(sum(x)/m))

#Athlete Sort
import math, os, random, re, sys
from operator import itemgetter
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr = sorted(arr, key=itemgetter(k))
    for l in arr:
        print(*l, sep = " ") 

#ginortS
s = input()
nums = [int(x) for x in s if x.isnumeric()]
even, odd = sorted([x for x in nums if x%2==0]), sorted([x for x in nums if x%2!=0])
print(
    ''.join(sorted([x for x in s if x.islower()]))+
    ''.join(sorted([x for x in s if x.isupper()]))+
    ''.join([str(x) for x in odd])+
    ''.join([str(x) for x in even])
)

################################################################# Python Functionals 

#Map and Lambda Function
cube = lambda x: x**3
def fibonacci(n):
    if n==0:
        return []
    if n==1:
        return [0]
    if n ==2:
        return [0, 1]    
    v = [0] * n
    v[1], v[2] = 1, 1
    for j in range(3,n):
        v[j] = v[j-1] + v[j-2]
    return v

################################################################# Regex and Parsing

#Detect Floating Point Number
n = int(input())
for x in range(n):
    m = input()
    try:
        float(m)
        if "." in [x for x in m]:
            print(True)
        else:
            print(False)    
    except Exception:
        print(False)

#Re.split()
regex_pattern = r"[,.]"

#Group(), Groups() & Groupdict()
import re
s = re.sub("[^a-zA-Z\d\s:]","#",input())
ctrl = True
for x in range(len(s)):
    if x!=len(s)-1 and s[x]!="#":
        if s[x+1]==s[x]:
            print(s[x])
            ctrl = False
            break
if ctrl:
    print(-1)

#Re.findall() & Re.finditer()
import re
vowels = ["A","E","I","O","U",]
consonants = "QWRTYPSDFGHJKLZXCVBNM"
s = input()
fin = []
subS = ""
for x in range(len(s)):
    if s[x].upper() in vowels:
        if len(subS)>=1:
            subS+=s[x]
        elif x!=0:
            if s[x-1].upper() in consonants:
                subS+=s[x]            
    else:
        if len(subS)>1:
            if x!=len(s)-1:
                if s[x].upper() in consonants:
                    fin.append(subS)
                    subS=""
                else:
                    subS=""
            elif x==len(s)-1:
               if s[x].upper() in consonants:
                    fin.append(subS)
                    subS=""
               else:
                    subS=""   
        else:
            subS=""  
if len(fin)>0:
    for x in fin:
        print(x)
else:
    print(-1)

#Re.start() & Re.end()
import re
ctrl=True
s, k = input(), input()
for x in range(len(s)):
    if s[x:x+len(k)] == k:
        print((x,x+len(k)-1))
        ctrl=False   
if ctrl:
    print((-1,-1))
 
#Regex Substitution
import re
for x in range(int(input())):
    s = input()
    if len(s)>0:
        s = re.sub(" ","  ",s)
        s = re.sub(" \\&\\& "," and ",s)
        s = re.sub(" \\|\\| "," or ",s)
        s = re.sub('  '," ",s)
        print(s)
        continue
    print(s)

#Validating Roman Numerals
'''Seeked for some help on stack overflow and some cheat sheets for the RegEx Syntax'''
import re
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
decine = '(X[CL]|L?X{0,3})'
unita = '(I[VX]|V?I{0,3})'
regex_pattern = thousand+hundred+decine+unita +"$"


#Validating phone numbers
import re
n = int(input())
for x in range(n):
    try:
        a=re.match(r'^[7,8,9]\d{9}$', input()).group(0)
        print("YES")
    except:
        print("NO")

#Validating and Parsing Email Addresses
import re
n=int(input())
for x in range(n):
    n, e = input().split()
    try:
        b=re.match('<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', e).group(0)
        print(n + " " + b)
    except AttributeError:
        pass
    
#Hex Color Code
import re
n = int(input())
openBracket = False
for x in range(n):
    s = re.sub("[;,():]"," ", input()).split()
    if openBracket: 
        for y in s:
            a=re.match("^#([A-fa-f0-9]{3}|[A-fa-f0-9]{6})$",y) 
            if a!=None:
                print(a.group(0))    
    try:                    
        if "{" in s:
            openBracket=True        
        if "}" in s:
            openBracket=False            
    except Exception:
        pass

#HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for x in attrs:
            print("->", x[0], ">", x[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for x in attrs:
            print("->", x[0], ">", x[1])  
parser = MyHTMLParser() 
n = int(input())
for x in range(n):
    s = input()
    parser.feed(s)

#HTML Parser - Part 2
from html.parser import HTMLParser
import re
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
             print(">>> Multi-line Comment")
             print(data)
        else:
             print(">>> Single-line Comment")
             print(data)    
    def handle_data(self, data):
        if len(re.sub("\n","",data))>0:
            print(">>> Data")
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'   
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values
n = int(input())
import re
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for x in attrs:
            print("->", x[0], ">", x[1])
parser = MyHTMLParser()           
for x in range(n):
    s = input()
    parser.feed(s)

#Validating UID
import re
n = int(input())
for _ in range(n):
    s = input()
    if len(s)!=10:
        print("Invalid")
    else:
        cc=0
        if re.search(r"([A-z].*){2}", s):
            cc+=1
        if re.search(r"([0-9].*){3}", s):
            cc+=1
        if re.search(r"[A-Za-z0-9]{10}", s):
            cc+=1
        if len(set([x for x in s]))==10:
            cc+=1
        if cc==4:
            print("Valid")
        if cc!=4:
            print("Invalid")
        cc=0

#Validating Credit Card Numbers
import re
for _ in range(int(input())):
    c = input()
    if isinstance(re.match(r"^[4-6]",c), type(None)):
        print("Invalid")
        continue
    if isinstance(re.match(r'^[0-9]{16}$', re.sub("-","",c)), type(None)):
        print("Invalid")
        continue 
    if isinstance(re.match("^[0-9-]*$", c), type(None)):
        print("Invalid")
        continue
    if isinstance(re.match(r"^([0-9]{16})|([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})$", c), type(None)):
        print("Invalid")
        continue
    c=re.sub("-","",c)    
    ctl=True
    for i in range(0,16-3):    
        if c[i]==c[i+1]==c[i+2]==c[i+3]:
            print("Invalid")
            ctl=False
            break
    if ctl:
        print("Valid")
    
#Validating Postal Codes
regex_integer_in_range = r"^[100000-999999]{6}$"
regex_alternating_repetitive_digit_pair = r"(?=(0.0))|(?=(1.1))|(?=(2.2))|(?=(3.3))|(?=(4.4))|(?=(5.5))|(?=(6.6))|(?=(7.7))|(?=(8.8))|(?=(9.9))"

#Matrix Script
import math, os, random, re, sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
s = "".join(["".join(x) for x in list(map(list, zip(*[[y for y in x] for x in matrix])))])
print(re.sub(r"(?<=([\w\d]))([ !@#$%&]{1,10000})(?=([\w\d]))"," ", s))
        
################################################################# XML

#XML 1 - Find the Score
def get_attr_number(node):
    s = [len(x.attrib) for x in root.iter()]
    return str(sum(s))

#XML2 - Find the Maximum Depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level+=1
    if level>=maxdepth:
        maxdepth=level
    for x in elem:
        depth(x, level)

################################################################# Closures and Decorations 

#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        ll=[]
        for x in l:
            if len(x)==10:
                ll.append("+91 {} {}".format(x[:5],x[5:]))
            elif len(x)==12:
                ll.append("+91 {} {}".format(x[-10:-5],x[-5:]))
            elif len(x)==11:
                ll.append("+91 {} {}".format(x[1:6],x[6:])) 
            elif len(x)==13:
                ll.append("+91 {} {}".format(x[-10:-5],x[-5:]))                
        ll.sort()        
        for x in ll:
            print(x)                                    
    return fun

#Decorators 2 - Name Directory
from operator import itemgetter
def person_lister(f):
    def inner(people):
        out= []
        for x in range(len(people)):
            people[x][2] = int(people[x][2])
        for x in sorted(people, key = itemgetter(2)):
            if x[-1] == "M":
                out.append("Mr. {} {}".format(x[0],x[1]))
            elif x[-1] == "F":
                out.append("Ms. {} {}".format(x[0],x[1]))
        return out            
    return inner

################################################################# Numpy

#Arrays
def arrays(arr):
    arr = numpy.array(arr)[::-1].astype(float)
    return arr

#Shape and Reshape
import numpy as np
print(np.reshape(np.array([int(x) for x in input().split()]), (3,3)))

#Transpose and Flatten
import numpy as np
n, m = list(map(int, input().split()))
arr = np.array([list(map(int, input().split())) for x in range(n)])
print(np.transpose(arr))
print(arr.flatten())

#Concatenate
import numpy as np
n, m, p = list(map(int, input().split()))
print(np.array([list(map(int, input().split())) for x in range(n+m)]))

#Zeros and Ones
import numpy as np
d = tuple(map(int, input().split()))
print(np.array(np.zeros(d, dtype = np.int)))
print(np.array(np.ones(d, dtype = np.int)))

#Eye and Identity
import numpy as np
np.set_printoptions(legacy="1.13")
n,m = list(map(int, input().split()))
print(np.eye(n, m))

#Array Mathematics
import numpy as np
n, m = list(map(int, input().split()))
a = np.array([list(map(int, input().split())) for x in range(n)], int)
b =  np.array([list(map(int, input().split())) for x in range(n)], int)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(a//b)
print(np.mod(a,b))
print(np.power(a,b))

#Floor, Ceil and Rint
import numpy as np
np.set_printoptions(sign=' ')
arr = np.array([x for x in input().split()], float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

#Sum and Prod
import numpy as np
n, m = list(map(int, input().split()))
arr = np.array([input().split() for x in range(n)], int)
print(np.prod(np.sum(arr, axis =0)))

#Min and Max
import numpy as np
n, m = list(map(int, input().split()))
arr=np.array([input().split() for _ in range(n)], int)
print(np.max(np.min(arr, axis=1)))

#Mean, Var, and Std
import numpy as np
n, m = list(map(int, input().split()))
arr = np.array([input().split() for _ in range(n)], int)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.around(np.std(arr, axis=None), 11))

#Dot and Cross
import numpy as np
n = int(input())
a, b = np.array([input().split() for _ in range(n)], int), np.array([input().split() for _ in range(n)], int)
print(np.dot(a,b))

#Inner and Outer
import numpy as np
a, b = np.array([input().split() for _ in range(2)], int)
print(np.inner(a, b))
print(np.outer(a,b))

#Polynomials
import numpy as np
arr, p = np.array(list(map(float, input().split()))), int(input())
print(np.polyval(arr, p))

#Linear Algebra
import numpy as np
n = int(input())
arr = np.array([list(map(float, input().split())) for _ in range(n)])
print(round(np.linalg.det(arr), 2))


'''
SOLUTIONS TO "PROBLEM 2" EXCERCISES
'''

#Birthday Cake Candles
import math, os, random, re, sys
def birthdayCakeCandles(candles):
    return candles.count(max(candles))  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

#Kangaroo/Number Line Jumps
import math, os, random, re, sys
def kangaroo(x1, v1, x2, v2):
    if x1==x2:
        return "YES"
    if v1==v2 and x1!=x2:
        return "NO"    
    if v1>v2 and x1>x2 or v1<v2 and x1<x2:
        return "NO"       
    for x in range(1,1000000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"    
    return "NO"      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

#Strange Advertising/Viral Advertising
import math, os, random, re, sys
def viralAdvertising(n): 
    c = 0
    recipients = 5
    for _ in range(n):
        c += math.floor(recipients/2)
        recipients = 3 * math.floor(recipients/2)
    return(c)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

#Recursive Digit Sum
import math, os, random, re, sys
def superDigit(n, k):
    p=0
    for x in range(len(n)):
       p+=int(n[x]) 
    while len(str(p))!=1:
        a = 0
        for x in range(len(str(p))):
            a+=int(str(p)[x])
        p = a
    return p        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

#Insertion Sort - Part 1
import math, os, random, re, sys
def insertionSort1(n, arr):
    e, arr = arr[-1], arr[:-1]
    p=0
    for x in range(len(arr)-1,-1,-1): 
        if arr[x]>e:
            arr.insert(x, arr[x])
            print(*arr, sep=" ")
            arr.remove(arr[x])
            p+=1
        elif arr[x]<=e:
            arr.insert(x+1, e) 
            print(*arr, sep=" ")   
            return None     
    if p==n-1:
        arr.insert(0, e)
        print(*arr, sep=" ")       
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

#Insertion Sort - Part 2
import math, os, random, re, sys
def insertionSort2(n, arr):
    l, arr, i = [arr[0]], arr[1:], 0
    for x in range(len(arr)):
        while arr[x] > l[i]:
            if len(l)==i+1:
                i+=1
                break
            i+=1
        l.insert(i, arr[x])
        print(*l+arr[x+1:], sep=" ")
        i=0 
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

#End
