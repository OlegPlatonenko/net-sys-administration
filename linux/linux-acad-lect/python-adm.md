# Python 3 for System Administration

## Table of contents

- [1. Install Dev Tools and Python 3 from source](#IDT)
- [2. Python 2 vs 3](#P2P3)
- [3. Script example and comments](#SEC)
- [4. Data Types in Python](#DAT)
    - [4.1 String](#STR)
    - [4.2 Int and Float](#IAF)
    - [4.3 Booleans and None](#BAN)
    - [4.3 Booleans and None](#BAN)
- [5. Variables](#VAR)
- [6. Lists](#LST)
- [7. Tuples](#TPL)
- [8. Dictionaries](#DIC)
- [9. Comparisons and Conditionals](#CAC)
- [10. While Loop](#WHL)
- [11. For Loop](#FOL)
- [12. Logic Operations](#LOG)
- [13. Reading User Input](#RUI)
- [14. Function Basics](#FBS)
- [15. Using Functions in Scripts](#UFS)
- [16. Using Standard Library Packages](#SLP)
- [17. Environment Variables](#EVS)
- [18. Interacting with Files](#IVF)
- [19. Parsing Command Line Parameters](#PCP)
- [20. Robust CLIs with 'argparse'](#RCW)
- [21. Handling Errors with try/except/else/finally](#HEW)
- [22. Exit Statuses](#ESS)
- [23. Execute Shell Commands from Python](#ESC)
- [24. Advanced Iteration with List Comprehensions](#AIL)

## 1. Install Dev Tools and Python 3 from source <a name="IDT"></a>

```
yum install -y \
> git \
> wget \
> which \
> words \
> lsof \
> vim
```

```bash
yum groupinstall -y "development tools"
yum install -y \
> libffi-devel \
> zlib-devel \
> bzip2-devel \
> openssl-devel \
> ncurses-devel \
> sqlite-devel \
> readline-devel \
> tk-devel \
> gdbm-devel \
> db4-devel \
> libpcap-devel \
> xz-devel \
> expat-devel 

cd /usr/src/
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar xf Python-3.6.5.tgz
cd Python-3.6.5/
./configure --enable-optimizations
make altinstall

chmod +w /etc/sudoers
sudo vim /etc/sudoers
#Search for secure_path
#Add at the end :/usr/local/bin
sudo pip3.6 install --upgrade pip
```

## 2. Python 2 vs 3 <a name="P2P3"></a>

- https://wiki.python.org/moin/Python2orPython3
- https://docs.python.org/3/whatsnew/3.0.html

## 3. Script example and comments <a name="SEC"></a>

- See hello.py in /scripts folder

## 4. Data Types in Python <a name="DAT"></a>

### 4.1 String <a name="STR"></a>

```python
#String in Python has 'str' type"

"Hello, World!"
"pass" + "word"
"Ha" * 3

"double".find('s')
"TeStInG".lower()

#Escape Sequences

print("Tab\tDelimeted")
print("New\nLine")
print("Slash\\Character")

print("'Single' are fine")
print('"Doble" are fine')
print('Your\'s are awesome')
```

### 4.2 Int and Float <a name="IAF"></a>

```python
#Adding
2 + 2

#Substruction
3 - 2

#Multiplying
3 * 2 

#Division
5 / 3
1.666666667

5 // 3
1

5 % 3
2

#Power
2 ** 3
8
```
```python
#Define type
type(3)
type("String")

int(1)
float(2.1)
str("Hello")
```

### 4.3 Booleans and None <a name="BAN"></a>

```python
True
type(True)
type(False)

#Nothingness
None
```

## 5. Variables <a name="VAR"></a>

```python
my_str = "This is a simple string"
my_str
print(my_str)

my_str += " testing"
my_str = my_str + "testing"

my_str = 1 #Variable type live changing
```

## 6. Lists <a name="LST"></a>

```python
#List examples
my_list = [1, 2, 3, 4, 5]
mix_list = [1, 'a', True]

#Call for list element
my_list[0]
my_list[-2]

#List length
len(my_list)

#Call for range
my_list[0:2]
my_list [1:]
my_list[:3]

#Takes step of 2 for each item
my_list[0::2]

#Set items
my_list[0] = 'a'

#Add to the list
my_list.append(6)

my_list + [8, 9, 10]
my_list += [8, 9, 10]

my_list[1:3] = ['b', 'c']
my_list[3:5] = ['d', 'e', 'f']

#Replace entire section with a nothing
my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
my_list[4:] = []

#Remove items from list
my_list.remove('b')
my_list.pop() #remove from the end
my_list.pop(0)#remove from the beginning
```

## 7. Tuples <a name="TPL"></a>

```python
#Plot using
point = (2.0, 3.0)

#Concatenation
point_3d = point + (4.0,)

#Tuple unpacking
x, y, z = point_3d

print("My name is: %s %s" % ("Oleg", "Platonenko"))
```

## 8. Dictionaries (dicts) <a name="DIC"></a>

```python
#Create Dictionary
ages ={ 'kevin': 49, 'alex': 29 'bob': 41 }

#Read value
ages['kevin']

#Assign value
ages['kayla'] = 21
ages['kayla'] = 22

#Remove thing
del ages['kevin']
ages.pop() #You need to provide argument
ages.pop('alex')

#Methods
ages.keys()
list(ages.keys())

ages.values()
list(ages.values())

#Alternative creation
weights = dict(kevin=160, bob=240, kayla=135)

#Create dictionary from Tuples
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
```

## 9. Comparisons and Conditionals <a name="CAC"></a>

```python
#Comparisons
1 < 2
True
0 > 2
False
2 == 1
False
2 != 1
True
3.0 >= 3.0
True
3.1 <= 3.0
False
1.1 == float("1.1")
True
'this' == 'this'
True
'b' > 'a'
True
'abc' < 'b'
True
2 in [1, 2, 3]
True
2 not in [1, 2, 3]
False
```

```python
#Conditionals
if 1 == 1: 
    print('this is true')

if False:
    print('was true')
else:
    print('was false')

name = 'Kevin'
if len(name) >= 6:
    print('name is long')
elif len(name) == 5:
    print('name is 5 characters')
elif len(name) >= 4:
    print('name is 4 or more')
else:
    print('name is short')
```

## 10. While Loop <a name="WHL"></a>

```python
while True:
    print('looping') #Infinite loop

count = 1
while count <= 4:
    print('looping')
    count += 1

count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}") #Run executable code inside of 'print' function
    count += 1

count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
```

## 11. For Loop <a name="FOL"></a>

```python
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

for color in colors:
    if color == 'blue'
        continue
    elif color == 'red'
        break
    print(color)

point = (2.1, 3.2, 7.7)
for value in point:
    print(value)

ages = {'kevin': 59, 'bob': 40, 'kayla':21}
for key in ages:
    print(key)

for letter in "my_string"
    print(letter)

#Unpack multiple items
list_of_points = [(1, 2), (2, 3), (4, 3)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")

ages = {'kevin': 59, 'bob': 40, 'kayla':21}
for name, age in ages.items():
    print(f"Person named: {name}")
    print(f"Age of: {age}")
```

## 12. Logic Operations <a name="LOG"></a>

```python
name = ""
not name

if not name:
    print("no Name givrn")

first = ""
last "Thompson"
if first or last:
    print("The user has a first or last name")

last = ""
last_name = last or "Doe"

first = "Keith"
last = ""
if first and last:
    print(f"Full name: {first} {last}")
elif first:
    print(f"First name: {first}")
elif last:
    print(f"Last name: {last}")
```

## 13. Reading User Input <a name="RUI"></a>

```python
#!/usr/bin/env python 3.6

name = input("What is your name? ")
birthdate = input("What is your birthday date? ")
age = int(input("How old are you? "))

print(f"{name} was born on {birthdate}")
print(f"Half of your age is {age / 2}")
```

## 14. Function Basics <a name="FBS"></a>

```python
def hello_world():
    print("Hello, World!")

#Function with input parameter
def print_name(name):
    print(f"Name is {name}")

#Function returns value
def add_two(num):
    return num + 2
```

## 15. Using Functions in Scripts <a name="UFS"></a>

- Look for bmi.py script in /scripts folder

## 16. Using Standard Library Packages <a name="SLP"></a>

- https://docs.python.org/3/library/index.html

```python
import time
now = time.localtime() #Time function
now.tm_hour #One of parameters

import time
from time import localtime, mktime, strftime #Import functions from class 'time'

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

#Wait for user to stop timer
input("Press 'Enter' to stop timer ")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
```

## 17. Environment Variables <a name="EVS"></a>

https://docs.python.org/3/library/os.html

```python
import os

#stage = os.environ["STAGE"].uper()
stage = os.getenv("STAGE", default="dev").upper()
output = f"We're running in {stage}"

if stage.startwith("PROD"):
    output = "Attention - " + output

print(output)
```

## 18. Interacting with Files <a name="IWF"></a>

```python
#Open function ('r' - read mode)
new_items = open('file_path', 'r')
new_items.read()

#Return cursor to beginning
new_items.seek(0)

#Read file using for loop
for line in new_items:
    print(line, end="")

#Close file after reading
new_items.close()
```

```python
#Open function ('w' - write mode)
new_items = open('file_path', 'w')
new_items.write(file_var.read())

new_items.open('file_path', 'r+') #Open for read/write
new_items.write("Test-string")

with open('file_path', 'a') as f:
    f.write("Test string")
```

## 19. Parsing Command Line Parameters <a name="PCP"></a>

```python
import sys
print(f"Positional arguments: {sys.argv[1:]}")
print(f"First argument: {sys.argv[1]}")
```

## 20. Robust CLIs with 'argparse' <a name="RCW"></a>

```python
import argparse

#ArgParser is a Class
parser = argparse.ArgumentParser(description='Read a file in reverse') 
#'filename' is positional (required) parameter, 'help=' -s help text, displays by -h
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

#parser_args method returns info taken from class
args = parser.parse_args()

#Open a file and read the lines
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip([::-1]))

print(args)

#Parse the arguments
#Read the file, reverse the contents and print
```

## 21. Handling Errors with try/except/else/finally <a name="HEW"></a>

```python

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip([::-1]))
```

## 22. Exit Statuses <a name="ESS"></a>

```python
#use script from previous units
import sys
#....
xcept FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
#...
```

## 23. Execute Shell Commands from Python <a name="ESC"></a>

```python
import subprocess
#Run 'ls -l' command
proc = subprocess.run(["ls", "-l"])

proc = subprocess.run(
    ["ls", "-l"], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    )
print(proc.stdout.decode())

new_proc = subprocess.run(['cat', 'fake.txt'])
new_proc = subprocess.run(['cat', 'fake.txt'], check=True)
```

## 24. Advanced Iteration with List Comprehensions <a name="AIL"></a>

```python
import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

#matches = []
#
#for word in words:
#    if snippet in word.lower():
#        matches.append(word)

print([word.strip() for word in words if snippet in word.lower()])

#print(matches)
```

