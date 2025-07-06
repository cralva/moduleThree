#inheritnace (you can inherit eyes or nose from parents. the parents pass those traits on to you)
#if grandpa dies and you inherit his land. He gave it to you
# it means getting something from someone else

#what does it mean in cpu programming?

class Parent():
    def print_last_name(self):
        print("Alvarez")

class Child(Parent): # The parenthese means we can take a previous class and their functions and add it into our new one. we just have to put the class name inside of the function
    def print_first_name(self):
        print("Cristian")
    
    def print_last_name(self): #this was added last/ we are overrode the the Parent class so we now have a new last name and the old one wont be in effect anymore. we just need to have the same function name
        print("shnizleberg")

Cristian = Child()
Cristian.print_first_name()
Cristian.print_last_name() #this will work because the child class inehrited the parent class. It will be with the same object

