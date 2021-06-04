# This is the oop code that I have leared step by step

class Game:
    def Work(self):
        return('This is not a game perhaps -_-')
    name = "There is no name of the game"

game1 = Game()

print(game1.Work())
print(game1.name)


class Human:
    name = "ahmed"
    def person(self):
        print("This is the fucation of the human you just called")
ahmed = Human()

ahmed.person()
print(ahmed.name)        


# THIS EG WILL BE using __init__ statement whih will just take arguments
#  that will run initially and we can use .slef to access it in other methods and variables
#we pass values that we use in init's parameters

class Anime:

    def __init__(self , name , rating):
        self.name = name
        self.rating = rating

    def stats(self):
        return f"the name of the anime is {self.name} and the rating of the anime is {self.rating}"

Naruto = Anime("Naruto" , 8.5)
OnePiece = Anime("One Piece" , 9)

print(Naruto.stats())
print(OnePiece.stats())


class constructor:
    def __init__(self):
        self.name = "ahmed"
        self.age = 17
    def call_const(self):
        p2.name = "not ahmed"
        p1.age = "1000"

p1 = constructor()
p2 = constructor()

p1.call_const()
p2.call_const()

print(p1.name)
print((p2.name))
print((p1.age))
print((p2.age))


# this is the example of the constructor
# we will use self. method to refer to the current object on which the funcation is applied
# or on which we are change the value.


class Compare:
    def __init__(self , name , age):
        self.name = name
        self.age = age


    def compare_obj(self , obj2):
        if self.name == obj2.name and self.age == obj2.age:
            print("THey are the same 0w0")
        else:
            print("they are not the same -_-") 
# name = input("Enter the Name: ")
# age = int(input("Enter the age: "))

# name2 = input("Enter the Name: ")
# age2 = int(input("Enter the age: "))

obj1 = Compare("name" , 77)
obj2 = Compare("name", 55)

obj1.compare_obj(obj2)
obj2.compare_obj(obj1)

# we have two kinds of variables instance and class variables.
# when we define a class variable we can use it anywhere in our class
# it will also affect all the things in the class related to that
# we have to define the class var before the init var
# also we have to do: classname.property = something

class var:
    one_piece_ep = 976
    def __init__(self):
        self.duration = "1999-idk what"
        self.rating = 8.5
anime1 = var()
anime2 = var()

anime1.duration = "I changed this 0w0"

var.one_piece_ep = 999

print(anime1.duration)
print(anime2.duration)
print(anime1.one_piece_ep)
print((anime2.one_piece_ep))


# in oop we are 3 methods for a function:
# instance , class and static methods

# This is the exmple of instace methods
# there are 2 things .. accessors (funcations which get data) and mutators(funcations which set data)
# if you need input from funcation / input you will use parameters in __init__ funcation

class Student():
    uni = "fast"

    def __init__(self , marks1 , marks2):
        self.marks1 = marks1
        self.marks2 = marks2
    # now I define use accessor here
    def get_marks(self):
        return(self.marks1 , self.marks2)
    # here is the mutator here
    def set_marks2(self , marks , marks_2):
        self.marks2 = marks
    #calculating the avg
    def avg(self):
        return(self.marks1 + self.marks2)/2

s1 = Student(22 , 34)
s2 = Student(45 , 56)


s1.set_marks2(22 , 56)
print(s1.get_marks())
print(s2.avg())

# new we will use class methods for class variables.
# and instad of slef. that we use in __init__ we use cls. that will refer to a class
# we will use @classmethod to define a class method -_-. or else we will have to pass the name of object

class CLS:
    school = "0w0"

    def __init__(self , name , age):
        self.name = name
        self.age = age
    def profile(self):
        return f"the name is {self.name} and age is {self.age} and the school is {CLS.school}"
    @classmethod
    def school_info(cls):
        return cls.school    
s1 = CLS("ahmed" , 17)
s2 = CLS("not ahmed" , 23)

s2.school = ":("

print(s1.profile())
print(s2.profile())
print(CLS.school_info())
print(CLS.school_info())
print(s2.school)

# NOW WE will work with static methods... like if we dont want to use variables
# and we dont want to use methods... like we want to do somethng different..
# then we will use static methods...


class Static:
    @staticmethod
    def owo():
        print(("This is a Static method -_-"))
owo1 = Static()
owo1.owo()

# this is how you create a class inside a class 0w0

class Nothing:
    def __init__(self , nothing , something):
        self.nothing = nothing
        self.something = something
        self.Nothingness = self.Nothingness()
    def show(self):
        print(self.nothing , self.something)
        self.Nothingness.show()
    class Nothingness:
        def __init__(self):
            self.nothingness = "+_+"
            self.void = "-_-"
        def show(self):
            print(self.nothingness , self.void)
    n = Nothingness()
    n.show()
    Nothingness.show(n)
    obj = Nothingness()
    obj2 = Nothingness()

new = Nothing("owo", 22)
new2 = Nothing("uwu", 12)

new.show()
new2.show()

idk = new.obj
ik = new2.obj2

new.obj.show()
new2.obj2.show()

idk.show()
ik.show()


# THis section is about inheritance and levels of inheritance
# this code is single level inheritance

class A:
    def f1(self):
        print("This is the feature 1")
    def f2(self):
        print("This is the feature 2")
class B(A):
        def f3(self):
            print("This is the feature 3")
        def f4(self):
            print("This is the feature 4")
a = A()
b = B()

a.f1()
a.f2()

b.f1()
b.f2()
b.f3()
b.f4()
    
# This is multi level inhertance :)
# here C inherits from A and also B +_+

class C(B):
    def f5(self):
        print("this is feature 5")
    def f6(self):
        print("this is feature 6")    
    
multi = C()

multi.f1()
multi.f2()
multi.f3()
multi.f4()
multi.f5()
multi.f6()

# now this is will an example of multiple level ineritance:

class D:
    def f1(self):
        print("This is the feature 1")
    def f2(self):
        print("This is the feature 2")
class E:
    def f3(self):
        print("This is the feature 3")
    def f4(self):
        print("This is the feature 4")
class F(D , E):
    def f5(self):
        print("This is feature 5")
    def f6(self):
        print("This is feature 6")
multiple = F()

multiple.f1()
multiple.f2()
multiple.f3()
multiple.f4()
multiple.f5()
multiple.f6()

# This is the an example of using __init__ (constructor) with inheritance.
# if there is no constructor in B then it will take it from A else it will render B 
# this vid also talks about ORM or whatever which goes from left to right.
# in this eg it goes left to right.

class A2:
    def __init__(self):
        print("this is the self thing -_- in A")
class C2:
    def __init__(self):
        print("this is the self thing -_- in c")
    def C(self):
        print("this is the self thing -_- in c")
class B2(A2 , C2):
    def __init__(self):
        super().__init__()
        super().C()
        print("This is from the B thing -_-")
b2 = B2()

    
# now here is an example of pylomorphism +_+
# idk what is it but lets find out what is it.
# pylo means MANY and morphism means FORMS.
# there are 4 ways to implement pylomorphism in python OOP.
# 1. duck typing -_-
# 2. Method overloading
# 3. Method Overloading
# 4. Method Overriding

#1 duck typing

class OnePiece:
    def typeowo(self):
        print("the type is shonen")
        print("the type is adventure")
        print("and its the best anime on the planet right now")

class Naruto:
    def typeowo(self):
        print("the type is shonen")
        print("the type is adventure")
        print("not the best in the world -_-")



class Anime:
    def Shonen(self , anime):
        anime.typeowo()
a5 = Anime()

anime = Naruto()

a5.Shonen(anime)