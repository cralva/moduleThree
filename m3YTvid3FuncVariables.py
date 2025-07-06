class Girl:
    
    gender = "Female" #class variable// every object that is created from this class will have this same variable (class) by default

    def __init__(self, name): #instance variable// we used "self" so its unique to each object.
        self.name = name

r = Girl("Rachel")
s = Girl("Jenna")

print(r.gender) #class variable is the same (Default)
print(s.gender)

print(r.name) #instance variable is going to be different (unique to the object)
print(s.name)