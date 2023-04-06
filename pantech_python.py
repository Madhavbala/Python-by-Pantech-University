#Day - 2

#Padding it means giving spaces on output
a = int(input(23))
b = int(input(23))
add = a+b
sub = a-b
mul = a*b
div = a/b
# print('{0:<4}|{0:<4}|{0:<4}|{0:>11}'.format(add,sub,mul,div))#here {0:<4} 0 is starting and 4 is ending 


course = "Pantech,Solutions Python" 
course = course.split()      #split always stores in list format
course = course.split(",") #split by comma
print(course)

Assign the number which all are near to 50
def myfunc(n):
  return abs(n-90)  #The Python abs() function return the absolute value and remove the negative sign of a number in Python.  

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

list1 = [1,2,3,4,5]
list2 = ["Madhavan","Mathu","Deepa","Balathandabani"]
# print(list2[2::])
con_string = list1+list2  #concatinate string
# print(len(con_string))

name = ['Madhavan','Mathu']
name.append('Deepa')
# print(name)

matrix_1 = [1,2,3]
matrix_2 = [4,5,6]
nested_list = [matrix_1,matrix_2]
# print(nested_list)
# print("nested list first row : ",nested_list[0])
# print("first element first row : ",nested_list[0][2])

numbers = [1,2,3,4,5,6]
numbers.reverse()
print(numbers)

print("Keys in dictionary must be unique in Dict and values may or may not br unique")
dicti = {"Name":"Madhavan","Age":21,"Company":["Saama","Tesla"]}   #key is Mutuable and Value is immutable so we use list also
print(dicti["Name"]) #In print way we use only one key to get values

mul_dic = {"Climate" : {"Condition" : {"Temperature" : 36, "Humidity": 50}}}
print(mul_dic["Climate"]["Condition"]["Humidity"])
print(mul_dic.keys())
print(mul_dic.values())
print(dicti.items()) #it shows every items in the dict

# List  --> Mutable  (Mutable means we can get watever we want)
# Tuple --> Imutable
# Set   --> Mutable(No Duplicate collections)
# Dict  --> Key must be unique 

#To add or update something
lis = ["Maddy"]
lis.append("Mathu")
print(lis)

sets = {'Mathu'}
sets.add('Maddy')
print(sets)

dicts = {"Name":"Mathu"}
dicts.update({"Age":20})
print(dicts)
get_val = dicts.get('Age')
print(get_val)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

pr = car.get("price", 15000) #It returns the value if it is not in particular dict just return and it doesn't effect the dict
print(pr)
print(car)

Day 3
Conditional statements
a = int(input("Enter the 1st Number : "))
b = int(input("Enter the 2nd Number : "))

if a>b:
    print("1st Statement")
elif a == b:
    print("2nd Statement")
else:
    print("3rd Statement")

a = [1,2,3]
for _ in a:
    print(_)

li = [x for x in range(5)]
print(li)

Dictionary For
dic_for = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for k,v in dic_for.items():
    print(k) #For Keys
    print(v) #For values

While
a = 0
while a < 10:
  # print(a)
  a+=1
  if a == 5:
    print("It's Five(5)")
    break
  else:
    print("Continue")

#For
for i in range(0,10,2):
  print(i)
a = [i for i in range(0,10,2)]
print(a)

b = [i for i in range(10,0,-2)] # if - is used the range should be in reverse order
# print(b)

pro = [ a for a in range(10) if a %2 == 0]
# print(pro)

string = "I'm Madhavan"
# vowels = []

for vowel in string:
    if vowel.lower() in "aeiou":
      print(vowel)
        # vowels.append(vowel.lower())
      pass
print(string,sep=',')


strings = "I'm Madhavan"
vowels = []

for vowel in strings:
    if vowel.lower() in "aeiou":
        vowels.append(vowel.lower())
# print(string,sep=',')
    


Enumerate
for i,a in enumerate("Mass Maddy"):
  print(i,a)

#Zip function
zip1 = ["Name","Age","Company"]
zip2 = ["Maddy",20,"Saama"]
whole = list(zip(zip1,zip2))
# print(whole)

di = [1,2,3,4]
dii = [1,5,6,7,8,9]
mer = di + dii
# print(set(mer)) #TO remove duplicate values

#Day 4
#Function

def welcome():
  print("Welcome to function")
# print(welcome())

#Fuction with arguments
def welcome(name):
  print(f"Welcome to the function {name}")
# welcome("Maddy")

#Print & Return
#Here use print
def add(a,b):
  print(a+b)
# add(5,5)

#Here return the value
def sub(a,b):
  return a-b
a = sub(4,5)
# print(a)


class student:

    school = "Sri Ragavendra Matriculation School"

    def __init__(self,tam,eng,mat,sci,soc):
        self.tam = tam
        self.eng = eng
        self.mat = mat
        self.sci = sci
        self.soc = soc 

    def avg(self):
        return (self.tam + self.eng + self.mat + self.sci + self.soc) / 5
    
    @classmethod       # to tells the compiler it is class set so we can call the method by using class name (the school vari used here)
    def sch(cls):
        return cls.school

    @staticmethod
    def static(): #this static method have no slef so it doesn't mean object or a class
        print("This static used to describe function without class and object(method) to run the method")

Madhavan = student(50,50,50,60,60)
Mathumitha = student(34,34,23,23,21)

# print(student.sch())
# print(student.static())

# Map function
def maps(numb):
  return numb**2

a = [1,2,3]
ans = list(map(maps,a))
# print(ans)


def add(num):
  return num+num

adds = [1,2,3,4,5]
anss = list(map(add,adds))
# print(anss)

def anal(num):
  return num % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(anal,nums)))
# print(list(filter(anal,nums)))  #Filter func high priority is only for true statements that is being comp one with another

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

# for x in adults:
#   print(x)


#Lambda funct using anonyms function without using def
#Lambda is only for particular func not suited for every function
       
      #keyword var : condition
lamb = lambda  num : num + num
# print(lamb(2))

# *args and *kwargs

# (Example *args)
def arg(a,b,c):
  add = a+b+c
  return add
# print(arg(12,12,12))  #Instead of doing this we use args

def args(*a):
  return sum(a)
# print(args(12,312,312,3,123,12))

def fun(first,*seconds):
  print("first Argument  : ",first)
  for arg in seconds:
    print(arg)
print(fun('Hello','Here','the','rest',"arguments"))


# **Kwargs it is same like args but it used to keep in assigned one (Keyword format)

def kwg(**kwargs):
  for keys,values in kwargs.items():
    pass
    # print(keys,values)
# print(kwg(Name='Maddy',Age = 20))


def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
      pass
        # print("%s == %s" % (key, value))
 
 
# Driver code
# myFun("Hi", first='Geeks', mid='for', last='Geeks')

# Class
class Student:
  print("Hello all")  #It alwasys print weater we did't call use method to avoid the print
x = Student()
print(type(x))

#Method calling
class Clg:
  def Mba():
    print("Master of Business Administraction")
# Clg.Mba()

#Self function to access something outside the class
class Sel:
  def One(self):
    print("Self function to access something that is outside the class")
x = Sel()    #Object call 
# x.One()

class Ass:
  year = '2023'           # if a variable is equal for every funct(method) we have to assign here
  def name():
    print("if a variable is equal for every funct(method) we have to assign here")

obj = Ass.name()
ye = Ass.year
print(ye)

class Cla:
  dob = '15.11.2001'
  def bir(self):
    print("Hello u r dob is : ",self.dob)
  
ob_call = Cla()
# ob_call.bir()

class Students:  #__init__ method it initialize attribute of an object(Whenever pass a one argument under class function the init itself you need to pass argument)
                 
  def __init__(self,name):
    self.name = name  #Attribute initialization

objects = Students(name = "Attribute Name")  #Creating instance of student class
# print(objects.name)

class Two:
  def __init__(self,name):
    self.name = name

#Here we use the multiple instance for one single class
first_instance = Two(name = 'Madhu')
second_instance = Two(name = 'Maddy')
print(first_instance.name)
print(second_instance.name)

class duo:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    # print(self.name)

  def __str__(self):
    return "hello madhavan"
  
mul_attri = duo(name="Mathu",age=23)
mul_attri.name = "Maddy"   
mul_attri.age =  21            #To change the values in the class
# print(mul_attri.name,mul_attri.age)

class College:
  total = 500

  def __init__(self,marks):
    self.marks = marks
    # self.total = 500

  def find_miss(self):
    return self.total - self.marks

  def percentage(self):
    return self.marks / self.total * 100

obj = College(marks = 234)
print("Student total marks : ",obj.marks)
print("Total marks         : ",obj.total)
print("Student loss marks  : ",obj.find_miss())
print("Student Percentage  : ",obj.percentage())

class Clg:
  total = 500
  def __init__(self,name,age,gender,marks):
    self.name = name
    self.age = age
    self.gender = gender
    self.marks = marks

  def __len__(self):  
    return self.marks 

  def __str__(self):
    return str(self.name) + str(self.gender)

  def __del__(self):
    pass
    # print("Deleted")

a = Clg(" Maddy ",20,"Male",450)

print(" Name : ",a.name,"Age : ",a.age,'Marks : ',len(a))
print(a)
del a

Derived class
class Elon:
  def __init__(self):
    # self.name = name
    # self.locaion = location
    print("Profile created")

  def name(self):
    print("Elon")
  
  def location(self):
    print("Coimbatore")
  

class Deriver_class(Elon):

  def __init__(self):
    Elon.__init__(self)
    print("Updated")

  def name(self):
    print("Musk")

  def location(self):
    print("America")

der_class = Deriver_class()
der_class.name()
der_class.location()


Polymorphism:
class Tesla:
  def __init__(self,name):
    self.name = name

  def type(self):
    return "Enterpernour"

class Google:
  def __init__(self,name):
    self.name = name

  def type(self):
    return "CEO"

Tesla_holder = Tesla("Elon Musk")
Google_holder = Google("Sundar Pichai")

for i in [Tesla_holder,Google_holder]:
  print(i.name,end=' - ')
  print(i.type())

Python Decorators
There is 2 way to initialize python decorators

''' 
First Type

@decName
def fun():
    print("Stamtement)

Second Type
def fun():
print("Statemnt)

funct = decNmae(func)

'''

Functions as object
def fun(a):
    print("Hello {0} welcome to python".format(a))

a = fun
a("Maddy")

Function in variable
def lowercase(texts):
    return texts.lower()

def uppercase(texts):
    return texts.upper()

def all(funct):
    variable = funct("Hello Buddy")
    print(variable)

all(lowercase)
all(uppercase)

Returning function from another function
def addmain(a):
    def add(b):
        print(a,b)
        return a + b
    return add

addition = addmain(100)
print(addition(56))


Decrators
def one(text):
    print("Start")
    text()         #here add the second function in middle of first function
    print("End")
    return text

def two():
    print("Middle")

deco = one(two)


class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
        
    def sub(self):
        return self.a - self.b

val = cal(2,4)
print(val.add())

def low(text):
    return text.lower()

def sec(texts):
    message = texts("MADHAVAN")
    print(message)

sec(low)

def sums(*args):
    return sum(args)

def numbers(num):
    numbe = num(1,2,3,4,5,6,7)
    print(numbe)

numbers(sums)

Iter it is the alternative function of for loop (format --> 1 - iter 2 - Next)
a = "champ"
for i in a:
    print(i)
next(a) #the value is string so it returns nothing

iterning = iter(a)
print(next(iterning))


my_iter = ["Madhavan","Bala","Deepa"]
itering = iter(my_iter)
print("First  one :",next(itering))
print("Second one :",next(itering))
print("Third  one :",next(itering))
print("It displays error :",next(itering)) #Because we have onl 3 values in list

Genarators
def square(n):
    for i in range(n):
        yield i**2

for n in square(10):
        print(n,end=' ')
